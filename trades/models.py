from django.db import models
from users.models import User

class Trade(models.Model):
    # Trade types: Buy or Sell
    TRADE_TYPE_CHOICES = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
    ]

    # Order types with advanced options like Stop, Trailing Stop, etc.
    ORDER_TYPE_CHOICES = [
        ('Market', 'Market'),
        ('Limit', 'Limit'),
        ('Stop', 'Stop'),
        ('Trailing Stop', 'Trailing Stop'),
        ('GTC', 'Good Till Cancelled'),
        ('FOK', 'Fill or Kill'),
    ]

    # Foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Trade and order details
    trade_type = models.CharField(max_length=10, choices=TRADE_TYPE_CHOICES)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, default='Market')
    stock_symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Support for fractional shares
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Pending')

    # String representation for the Trade model
    def __str__(self):
        return f"{self.user.username} - {self.trade_type} {self.stock_symbol} ({self.quantity})"

    # Method to execute trade based on order type
    def execute_trade(self):
        # Handle different trade types and order execution logic
        if self.order_type == 'Market':
            self._execute_market_order()
        elif self.order_type == 'Limit':
            self._execute_limit_order()
        elif self.order_type == 'Stop':
            self._execute_stop_order()
        # Add more logic for other order types...
        self.save()

    # Private method to handle market orders
    def _execute_market_order(self):
        if self.trade_type == 'Buy':
            cost = self.quantity * self.price
            if self.user.portfolio_balance >= cost:
                self.user.update_balance(-cost)
                self.status = 'Executed'
                self.user.experience_points += 100  # Award experience points for successful trade
                self.user.calculate_user_level()
                self.user.save()
            else:
                self.status = 'Failed'
                raise ValueError("Insufficient balance to execute buy trade.")
        elif self.trade_type == 'Sell':
            revenue = self.quantity * self.price
            self.user.update_balance(revenue)
            self.status = 'Executed'
            self.user.experience_points += 100
            self.user.calculate_user_level()
            self.user.save()
        else:
            raise ValueError("Invalid trade type.")
