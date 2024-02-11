from django.shortcuts import render
from .serializers import DepositSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
# Create your views here.
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
