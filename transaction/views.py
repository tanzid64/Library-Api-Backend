from django.shortcuts import render
from .serializers import DepositSerializer, BuyBookSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Transaction
from book.models import Book
# Create your views here.
class DepositView(APIView):
    # permission_classes = [IsAuthenticated]
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
    # permission_classes = [IsAuthenticated]

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

                data = {'amount': amount, 'book': book_id, 'type': 'Purchase'}
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Insufficient Balance.'}, status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            return Response({'error': 'Low Quantity.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        