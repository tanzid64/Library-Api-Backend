from rest_framework import serializers
from .models import Transaction
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

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
    class Meta:
        model = Transaction
        fields = "__all__"


