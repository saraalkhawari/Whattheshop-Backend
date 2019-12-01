from django.urls import path

#pick one way to import views?
from .views import UserCreateAPIView, DetailView
from api import views

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
	path('', views.CreaturesList.as_view(), name="list"),
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register')
]