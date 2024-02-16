from django.shortcuts import render
from .serializers import OpenPublisherSerializer, AllPublisherSerializer, EditPublisherSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsAdminOrOwner
from .models import Publisher
# Create your views here.
class OpenPublisherView(CreateAPIView):
    serializer_class = OpenPublisherSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminOrOwner]

    def perform_create(self, serializer):
        if 'logo' in self.request.data: 
            image = self.request.data['logo']  
            serializer.validated_data['logo'] = image
        serializer.save(owner=self.request.user)

class AllPublisherView(ListAPIView):
    serializer_class = AllPublisherSerializer
    queryset = Publisher.objects.all()

class PublisherUpdateView(RetrieveUpdateAPIView):
    serializer_class = EditPublisherSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminOrOwner]
    def get_object(self):
        return Publisher.objects.get(pk=self.kwargs['pk'])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def perform_update(self, serializer):
        if 'logo' in self.request.data:  
            image = self.request.data['logo']  
            serializer.validated_data['logo'] = image
        serializer.save(owner=self.request.user)