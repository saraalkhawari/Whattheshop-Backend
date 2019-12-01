from rest_framework.permissions import AllowAny
from .serializers import CreatureSerializer, UserCreateSerializer
from .models import Creature
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

class CreaturesList(ListAPIView):
	queryset = Creature.objects.all()
	serializer_class = CreatureSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
