from django.shortcuts import render
import uuid
from .serializers import DepositSerializer, BuyBookSerializer, TransactionReportSerializer, CartAddSerializer, CartSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Transaction, Cart
from book.models import Book
# Create your views here.
class CartView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    def get_serializer_class(self):
        if self.request.method == "GET":
            return  CartSerializer
        return CartAddSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quantity = serializer.validated_data.get("quantity")
        book_id = serializer.validated_data.get("book")
        try:
            book = Book.objects.get(id=book_id)
            print(book.title)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        if book.quantity >= quantity:
            Cart.objects.create(
                user=request.user,
                book=book,
                quantity=quantity,
            )
            return Response({"message": f"{book.title} successfully added to cart."}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Low Quantity.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        
    def list(self, request, *args, **kwargs):        
        queryset = Cart.objects.filter(user=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        quantity = serializer.validated_data.get("quantity")
        instance.quantity = quantity
        instance.save()
        return Response(serializer.data)



class DepositView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            user = request.user
            if user.is_authenticated:
                user.balance += amount
                user.save()
                transaction = Transaction.objects.create(
                    user = user,
                    amount = amount,
                    type = "Deposit"
                )
                transaction.save()
                return Response({"message": "Deposit successful"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyBookAPIView(generics.CreateAPIView):
    serializer_class = BuyBookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get('book')
        book = Book.objects.get(pk=book_id)
        if book.quantity > 0:
            user = self.request.user
            if user.balance >= book.price:
                amount = book.price
                
                user.balance -= amount
                user.save()
                publisher = book.publisher
                publisher.balance += amount
                publisher.save()
                book.quantity -= 1
                book.save()

                data = {'amount': amount, 'book': book_id, 'type': 'Purchase'}
                serializer = self.get_serializer(data=data, context = {'amount':amount, 'user':user})
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user)
                return Response({'success': 'Purchase Successfull'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Insufficient Balance.'}, status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            return Response({'error': 'Low Quantity.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
class TransactionReport(generics.ListAPIView):
    serializer_class = TransactionReportSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user = self.request.user)
    

        