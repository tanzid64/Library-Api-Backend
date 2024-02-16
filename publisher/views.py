from django.shortcuts import render
from .serializers import OpenPublisherSerializer, AllPublisherSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner
from .models import Publisher
# Create your views here.
class OpenPublisherView(CreateAPIView):
    serializer_class = OpenPublisherSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminOrOwner]

    def perform_create(self, serializer):
        if 'logo' in self.request.data:  # Use 'logo' instead of 'image'
            # Handle image upload
            image = self.request.data['logo']  # Use 'logo' instead of 'image'
            serializer.validated_data['logo'] = image
        serializer.save(owner=self.request.user)

class AllPublisherView(ListAPIView):
    serializer_class = AllPublisherSerializer
    queryset = Publisher.objects.all()