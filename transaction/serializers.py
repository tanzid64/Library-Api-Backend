

from rest_framework import serializers

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(decimal_places=2, max_digits=12)
