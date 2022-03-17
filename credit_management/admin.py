from django.contrib import admin
from credit_management.models import CreditManagement


@admin.register(CreditManagement)
class CreditManagementAdmin(admin.ModelAdmin):
    pass
