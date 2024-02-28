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
from django.db.models import Sum
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
                    type = "Deposit",
                    book = None
                )
                transaction.save()
                return Response({"message": "Deposit successful"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Order Plce helping function
def buy_book(item,user):
    book = item.book
    publisher = book.publisher
    user.balance -= item.amount
    user.save() # Update User Balance
    publisher.balance += item.amount
    publisher.save() # Update publisher balance
    book.quantity -= item.quantity
    book.save() # Update Book quantity
    Transaction.objects.create( # Create Transaction History
        user = user,
        book = book,
        type = 'Purchase',
        amount = item.amount
    )
    item.delete() # Removing from Cart 
class PlaceOrderView(generics.CreateAPIView):
    serializer_class = BuyBookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.filter(user=user)
        # Checking Cart is empty or not
        if len(cart) == 0:
            return Response(
                {'error': 'Your Cart is empty.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_amount = cart.aggregate(total_amount=Sum('amount'))['total_amount']
        # Check User balance availability
        print(user.username)
        if total_amount > user.balance:
            return Response(
                {'error': 'Insufficient Balance. Please deposite money.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Check Book stock
        for item in cart:
            book = item.book
            if book.quantity < item.quantity:
                return Response(
                        {'error': f"{book.title} is low stock."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
        # Place Order
        for item in cart:
            buy_book(item, user)
        return Response(
            {'message': 'Order placed successfully.'},
            status=status.HTTP_201_CREATED
        )

class TransactionReport(generics.ListAPIView):
    serializer_class = TransactionReportSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user = self.request.user)
    