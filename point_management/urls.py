from django.urls import path, include
from rest_framework.routers import DefaultRouter

from point_management.views import PointManagementViewSet

app_name = "point_management"

router = DefaultRouter()
router.register("point_management", PointManagementViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]