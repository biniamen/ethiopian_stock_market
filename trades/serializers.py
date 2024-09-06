from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['id', 'user', 'trade_type', 'stock_symbol', 'quantity', 'price', 'trade_date']
