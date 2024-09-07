from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Meta class to define model fields to be serialized
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'portfolio_balance', 'password', 'kyc_document', 'kyc_verified', 'experience_points', 'user_level']
        extra_kwargs = {'password': {'write_only': True}}

    # Override the create method to handle default portfolio balance
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.portfolio_balance = 100000.00  # Set default portfolio balance
        user.save()
        return user
