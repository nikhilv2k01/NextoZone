from rest_framework import serializers
from .models import *
from .models import *
from django.db.models import Q


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['user_id', 'user_name', 'password', 'email_id', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        """
        Verify Email or Username already exists
        """
        queryset = Register.objects.filter(
            Q(user_name=attrs['user_name']) | Q(email_id=attrs['email_id']))
        if queryset:
            raise serializers.ValidationError(
                {"message": "Username or Email-Id already exists."})
        return attrs


# Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['user_name', 'password']

    def validate(self, attrs):
        """
        verify Login credentials is valid.
        """
        user_name = attrs['user_name']
        password = attrs['password']

        if '@' in user_name:
            username_exist = Register.objects.filter(
                email_id=user_name).exists()
        else:
            username_exist = Register.objects.filter(
                user_name=user_name).exists()

        password_exist = Register.objects.filter(password=password).exists()

        if not username_exist:
            raise serializers.ValidationError({"message": "User not found!"})
        if not password_exist:
            raise serializers.ValidationError(
                {"message": "Incorrect password!"})
        return attrs
