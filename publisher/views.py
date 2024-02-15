from django.shortcuts import render
from .serializers import OpenPublisherSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
class OpenPublisherView(CreateAPIView):
    serializer_class = OpenPublisherSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        if 'logo' in self.request.data:  # Use 'logo' instead of 'image'
            # Handle image upload
            image = self.request.data['logo']  # Use 'logo' instead of 'image'
            serializer.validated_data['logo'] = image
        serializer.save(owner=self.request.user)