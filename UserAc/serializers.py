from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MyUser

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'full_name', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser.objects.create_user(**validated_data, password=password)
        return user


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        data['user'] = user
        return data