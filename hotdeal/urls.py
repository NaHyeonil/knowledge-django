from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hotdeal.views import HotdealViewSet

app_name = "hotdeal"

router = DefaultRouter()
router.register("hotdeal", HotdealViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
