from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from account.backends import CustomAuthenticationBackend

from . models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


# user serializer
class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False, allow_null=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "full_name", "phone", "image", "is_user", "auth_type", "is_verified", "password"]
        read_only_fields = ["is_user", "is_verified", "auth_type"]
        extra_kwargs = {
                    'password': {'write_only': True}
                }
        
    def create(self, validated_data):
        image = None
        if "image" in validated_data.keys():
            image = validated_data['image']
        user = User.objects.create(
                    username=validated_data['username'],
                    email=validated_data['email'],
                    is_user=True,
                    is_verified=False,
                    image=image
                )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # set email to read only on update
    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields['email'].read_only = True
        return fields
    
    
class UpdateUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False, allow_null=True)
    class Meta:
        model= User
        fields = ["id", "username", "email", "full_name", "phone", "image", 'is_user', "is_verified", 'is_admin']
        read_only_fields = ['email', 'is_user', 'is_verified', 'is_admin']




class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)