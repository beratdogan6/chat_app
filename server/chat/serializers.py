from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Profile


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        # Profile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    photo = serializers.ImageField(source='profile.photo')
    online = serializers.BooleanField(source='profile.online')
    status = serializers.CharField(source='profile.status')

    class Meta:
        model = User
        fields = ('name', 'username', 'photo', 'online', 'status')

    def get_name(self, obj):
        if obj.first_name:
            return obj.get_full_name()
        return obj.username
