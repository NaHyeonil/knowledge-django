from django.urls import path, include
from rest_framework.routers import DefaultRouter

from knowledge_share.views import Knowledge_ShareViewSet

app_name = "knowledge_share"

router = DefaultRouter()
router.register("knowledge_share", Knowledge_ShareViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
