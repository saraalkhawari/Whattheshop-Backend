from django.urls import path

#pick one way to import views?
from api import views

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
	path('', views.CreaturesList.as_view(), name="list"),
	path('history/', views.OrderHistoryList.as_view(), name="history"),
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
    path('checkout/', views.CheckoutView.as_view(), name="checkout"),
    path('wigs/', views.WigList.as_view(), name="wig"),
    path('creaturewigs/', views.CreatureWigList.as_view(), name="creaturewig"),

]


