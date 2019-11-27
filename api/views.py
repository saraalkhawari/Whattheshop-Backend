from rest_framework.generics import CreateAPIView
from .serializers import CreatureSerializer,UserCreateSerializer

from .models import Creature
from rest_framework.generics import ListAPIView



class CreaturesList(ListAPIView):
	queryset = Creature.objects.all()
	serializer_class = CreatureSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
