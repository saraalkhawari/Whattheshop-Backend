from django.contrib import admin
from .models import Creature, Cart, CartItem

admin.site.register(Creature)
admin.site.register(Cart)
admin.site.register(CartItem)
