from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = user
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model()(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
