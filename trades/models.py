from django.db import models
from users.models import User

class Trade(models.Model):
    TRADE_TYPE_CHOICES = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=10, choices=TRADE_TYPE_CHOICES)
    stock_symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.trade_type} {self.stock_symbol} ({self.quantity})"
