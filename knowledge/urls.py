from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('knowledge/', include('knowledge_share.urls')),
    path('hotdeal/', include('hotdeal.urls')),
    path('notice/', include('notice.urls')),
    path('point/', include('point_management.urls')),
    path('trade/', include('trade.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)