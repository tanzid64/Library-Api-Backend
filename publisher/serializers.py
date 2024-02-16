from rest_framework import serializers
from .models import Publisher

class OpenPublisherSerializer(serializers.ModelSerializer):
    # logo = serializers.ImageField(required=False, source='image')
    class Meta:
        model = Publisher
        fields = ['name', 'logo', 'address']

class AllPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"