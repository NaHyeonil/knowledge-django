from django.contrib import admin

from trade.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    pass
