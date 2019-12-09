from django.contrib import admin
from .models import Creature, Cart, CartItem, Wig, CreatureWig

admin.site.register(Creature)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wig)
admin.site.register(CreatureWig)


