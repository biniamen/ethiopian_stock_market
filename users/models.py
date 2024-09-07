# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Trader', 'Trader'),
        ('Broker', 'Broker'),
        ('MarketMaker', 'Market Maker'),
        ('Regulator', 'Regulator'),
        ('Investor', 'Investor'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    portfolio_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # New Field

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def update_balance(self, amount):
        self.portfolio_balance += amount
        self.save()

