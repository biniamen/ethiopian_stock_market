# stock_market_app/urls.py

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/users/', include('users.urls')),  # Updated URL pattern
    path('api/trades/', include('trades.urls')),  # Updated URL pattern
    path('api-token-auth/', obtain_auth_token),  # Endpoint for obtaining tokens
]
