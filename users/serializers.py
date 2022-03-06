from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class EcoRegisterSerializer(RegisterSerializer):

    username = None
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }


class EcoLoginSerializer(LoginSerializer):

    username = None


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
