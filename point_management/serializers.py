from rest_framework import serializers

from point_management.models import PointManagement


class PointManagementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointManagement
        fields = "__all__"


class PointManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointManagement
        fields = "__all__"
        depth = 1