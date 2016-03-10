
from rest_framework import serializers

from django.contrib.auth.models import User
from app.blogApp.jwt_helper import get_json_web_token



class LoginSerializer(serializers.ModelSerializer):
    """
        Account Signup serializer to handle user registration.
    """
    token = serializers.SerializerMethodField('get_json_web_token')

    class Meta:
        model = User
        fields = ('token',)

    def get_json_web_token(self, obj):
        """
            Returns json web token for the user object
        """
        return get_json_web_token(obj)


