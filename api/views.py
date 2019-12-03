from rest_framework.permissions import AllowAny
from .serializers import CreatureSerializer,CartSerializer, UserCreateSerializer, AddToCartSerializer
from .models import Creature, Cart , CartItem
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

class CreaturesList(ListAPIView):
	queryset = Creature.objects.all()
	serializer_class = CreatureSerializer

class CartList(ListAPIView):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class AddToCart(CreateAPIView):
	serializer_class = AddToCartSerializer

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])
