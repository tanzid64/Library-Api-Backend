from django.shortcuts import render
from .serializers import DepositSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class DepositView(APIView):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)