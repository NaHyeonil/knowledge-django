from rest_framework import serializers

from credit_management.models import CreditManagement


class CreditManagementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditManagement
        fields = "__all__"


class CreditManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditManagement
        fields = "__all__"
        depth = 1
