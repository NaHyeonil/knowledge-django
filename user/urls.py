from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserAPIView, UserViewSet

app_name = "user"

urlpatterns = []

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns += [path('api/user/', UserAPIView.as_view(), name='user'),
                ]