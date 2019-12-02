from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
	path('', views.CreaturesList.as_view(), name="list"),
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
]