from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trade.views import TradeViewSet

app_name = "trade"

router = DefaultRouter()
router.register("trade", TradeViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
