from django.urls import path, include
from rest_framework.routers import DefaultRouter

from credit_management.views import CreditManagementViewSet

app_name = "credit_management"

router = DefaultRouter()
router.register("credit_management", CreditManagementViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
