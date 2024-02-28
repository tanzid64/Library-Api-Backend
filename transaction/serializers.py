from rest_framework import serializers
from .models import Transaction
from .models import Cart
from book.serializers import BookSerializer

class CartSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"
    def get_book(self, obj):
        return obj.book.title 

class CartAddSerializer(serializers.Serializer):
    book = serializers.UUIDField()
    quantity = serializers.IntegerField(required=True)

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(decimal_places=2, max_digits=12)

class BuyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [ 'book']

    def create(self, validated_data):
        user = self.context['user']
        amount = self.context['amount']
        validated_data['user'] = user
        validated_data['type'] = 'Purchase'
        validated_data['amount'] = amount
        return super().create(validated_data)
    
class TransactionReportSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()  # Define a SerializerMethodField for book

    class Meta:
        model = Transaction
        fields = "__all__"
    
    def get_book(self, obj):
        if obj.book:
            return obj.book.title  # Retrieve the title of the associated book



