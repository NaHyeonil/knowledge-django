from django.contrib import admin
from hotdeal.models import Hotdeal


@admin.register(Hotdeal)
class HotdealAdmin(admin.ModelAdmin):
    pass
