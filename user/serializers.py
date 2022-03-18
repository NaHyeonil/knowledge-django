from typing import Dict
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)


from notice.serializers import NoticeSerializer


User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["user_id", "password", "password2", "username",
                  "nickname", "phone_num", "email"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Difference between passwords")
        return attrs

    def create(self, validated_data):
        user_id = validated_data["user_id"]
        username = validated_data["username"]
        password = validated_data["password"]
        nickname = validated_data.get("nickname", "")
        phone_num = validated_data["phone_num"]
        email = validated_data["email"]
        new_user = User(user_id=user_id, username=username, nickname=nickname, phone_num=phone_num, email=email,)
        new_user.set_password(password)
        new_user.save()
        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["user_id"] = self.user.user_id
        data["username"] = self.user.username
        data["nickname"] = self.user.nickname
        data["is_staff"] = self.user.is_staff
        data["is_superuser"] = self.user.is_superuser
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    notice_set = NoticeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["user_id", "is_superuser", "is_staff", "username", "nickname",
                  "phone_num", "notice_set", "is_active"]
