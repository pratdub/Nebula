from rest_framework import serializers
from .models import User, OTP

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class OtpSerializer(serializers.ModelSerializer) :
    class Meta:
        model = OTP
        fields = '__all__'


class LoginSerializer(serializers.Serializer) :
    email = serializers.CharField()
    password = serializers.CharField()
