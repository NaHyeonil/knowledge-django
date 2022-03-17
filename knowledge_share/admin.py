from django.contrib import admin
from knowledge_share.models import Knowledge_Share


@admin.register(Knowledge_Share)
class Knowledge_ShareAdmin(admin.ModelAdmin):
    pass
