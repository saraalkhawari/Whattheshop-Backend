from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Creature, Cart, CartItem

class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = ['id','name','origin','description','wig','price','image']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','creature','quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['cart_items','date']

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['creature']

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

