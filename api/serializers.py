from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Creature

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = ['name', 'origin', 'description', 'price', 'image',]