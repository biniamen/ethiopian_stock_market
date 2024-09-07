from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),  # Endpoint for user login and token generation
    path('users/', include('users.urls')),
    path('trades/', include('trades.urls')),
]
