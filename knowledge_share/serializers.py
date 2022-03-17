from rest_framework import serializers

from knowledge_share.models import Knowledge_Share


class Knowledge_ShareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge_Share
        fields = "__all__"


class Knowledge_ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge_Share
        fields = "__all__"
        depth = 1
