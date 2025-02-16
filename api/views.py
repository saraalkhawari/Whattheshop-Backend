from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import CreatureSerializer, UserCreateSerializer,OrderHistorySerializer, CheckoutSerializer, WigSerializer, CreatureWigSerializer
from .models import Creature, Cart , CartItem, Wig, CreatureWig
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .permissions import IsCartUser


class WigList(ListAPIView):
	queryset = Wig.objects.all()
	serializer_class = WigSerializer 

class CreaturesList(ListAPIView):
	queryset = Creature.objects.all()
	serializer_class = CreatureSerializer 

class CreatureWigList(ListAPIView):
	queryset = CreatureWig.objects.all()
	serializer_class = CreatureWigSerializer

class OrderHistoryList(ListAPIView):
	serializer_class = OrderHistorySerializer
	permission_classes = [IsAuthenticated]
	
	def get_queryset(self):
		return Cart.objects.filter(user=self.request.user)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CheckoutView(CreateAPIView):
	serializer_class = CheckoutSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
