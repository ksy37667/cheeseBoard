from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
            'password': {'required': True}
        }

        def create(self, validated_data):
            user = User.objects.create(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])

            user.save()
            return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")