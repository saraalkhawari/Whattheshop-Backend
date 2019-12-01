from django.urls import path
from .views import UserCreateAPIView, DetailView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('detail/<int:object_id>/', DetailView.as_view(), name='detail'),
]