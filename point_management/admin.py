from django.contrib import admin
from point_management.models import PointManagement


@admin.register(PointManagement)
class PointManagementAdmin(admin.ModelAdmin):
    pass