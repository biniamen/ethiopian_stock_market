from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()  # Retrieve all trade objects
    serializer_class = TradeSerializer  # Use TradeSerializer for data serialization

    # Override the create method to execute trade and handle errors
    def perform_create(self, serializer):
        trade = serializer.save()  # Save trade data
        try:
            trade.execute_trade()  # Execute the trade
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    # Endpoint to retrieve all active (pending) trades
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def active_trades(self, request):
        trades = Trade.objects.filter(status='Pending')  # Filter pending trades
        serializer = self.get_serializer(trades, many=True)
        return Response(serializer.data)
