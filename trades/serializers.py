from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
    # Meta class to define model fields to be serialized
    class Meta:
        model = Trade
        fields = ['id', 'user', 'trade_type', 'order_type', 'stock_symbol', 'quantity', 'price', 'trade_date', 'status']
