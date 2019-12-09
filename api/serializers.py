from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Creature, Cart, CartItem, Wig

class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = ['id','name','origin','description','wig','price','image']

class WigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wig
        fields = ['id','color','image']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['creature','quantity']

class OrderHistorySerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['user','cart_items','date']

class CheckoutSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many = True)

    class Meta:
        model = Cart
        fields = ['cart_items']

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)
        for data in cart_items_data:
            CartItem.objects.create(cart=cart, **data)
        return cart


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

