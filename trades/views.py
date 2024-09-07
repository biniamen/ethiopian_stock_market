from rest_framework import viewsets, permissions
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    def perform_create(self, serializer):
        trade = serializer.save()
        trade.execute_trade()  # Call method to execute trade