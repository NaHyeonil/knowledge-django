from rest_framework import serializers

from hotdeal.models import Hotdeal


class HotdealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotdeal
        fields = "__all__"


class HotdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotdeal
        fields = "__all__"
        depth = 1
