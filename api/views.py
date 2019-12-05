from rest_framework.permissions import AllowAny
from .serializers import CreatureSerializer,CartSerializer, UserCreateSerializer, AddToCartSerializer
from .models import Creature, Cart , CartItem
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .permissions import IsCartUser

class CreaturesList(ListAPIView):
	queryset = Creature.objects.all()
	serializer_class = CreatureSerializer

class CartList(ListAPIView):
	serializer_class = CartSerializer
	def get_queryset(self):
		return Cart.objects.filter(user=self.request.user)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class AddToCart(CreateAPIView):
	serializer_class = AddToCartSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
