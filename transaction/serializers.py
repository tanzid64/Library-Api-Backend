

from rest_framework import serializers
from .models import Transaction


class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(decimal_places=2, max_digits=12)

class BuyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'book']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['type'] = 'Purchase'
        return super().create(validated_data)

