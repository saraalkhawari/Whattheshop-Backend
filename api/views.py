from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, DetailSerializer
from api.models import Creature
from rest_framework.permissions import AllowAny

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class DetailView(RetrieveAPIView):
    queryset = Creature.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [AllowAny]
