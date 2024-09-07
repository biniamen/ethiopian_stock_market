from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Role choices for different user types
    ROLE_CHOICES = [
        ('Trader', 'Trader'),
        ('Broker', 'Broker'),
        ('MarketMaker', 'Market Maker'),
        ('Regulator', 'Regulator'),
        ('Investor', 'Investor'),
    ]

    # User role field
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Portfolio balance for users, initialized to 100,000 Birr
    portfolio_balance = models.DecimalField(max_digits=15, decimal_places=2, default=100000.00)

    # KYC document file field and verification status
    kyc_document = models.FileField(upload_to='kyc_documents/', null=True, blank=True)
    kyc_verified = models.BooleanField(default=False)

    # Fields to manage user experience and levels (gamification)
    experience_points = models.IntegerField(default=0)
    user_level = models.IntegerField(default=1)

    # Custom groups and permissions for users
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

    # Method to update portfolio balance
    def update_balance(self, amount):
        self.portfolio_balance += amount
        self.save()

    # Method to calculate user level based on experience points
    def calculate_user_level(self):
        self.user_level = self.experience_points // 1000  # Example: 1000 XP = Level 2
        self.save()
