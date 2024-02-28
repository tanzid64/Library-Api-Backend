from rest_framework import serializers
from .models import Publisher
from book.serializers import BookSerializer

class OpenPublisherSerializer(serializers.ModelSerializer):
    # logo = serializers.ImageField(required=False, source='image')
    class Meta:
        model = Publisher
        fields = ['name', 'logo', 'address']

class EditPublisherSerializer(serializers.ModelSerializer):
    # book = BookSerializer(many=True)
    # id = serializers.UUIDField()
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'logo', 'address']
    def __init__(self, *args, **kwargs):
        super(EditPublisherSerializer, self).__init__(*args, **kwargs)
        # Make fields optional for partial updates
        for field_name in self.fields.keys():
            self.fields[field_name].required = False

class AllPublisherSerializer(serializers.ModelSerializer):
    # book = BookSerializer(many=True)
    class Meta:
        model = Publisher
        # exclude = ['balance']
        fields = ['id', 'created_at', 'name', 'logo', 'address']