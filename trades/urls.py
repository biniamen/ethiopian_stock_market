# trades/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradeViewSet

router = DefaultRouter()
router.register(r'', TradeViewSet)  # Empty prefix

urlpatterns = [
    path('', include(router.urls)),
]
