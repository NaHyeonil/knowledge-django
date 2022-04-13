from rest_framework import serializers

from trade.models import Trade


class TradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"
        depth = 1
