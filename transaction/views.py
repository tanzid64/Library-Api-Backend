from django.shortcuts import render
from .serializers import DepositSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class DepositView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validate_data['amount']
            user = request.user
