from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Creature(models.Model):
	name = models.CharField(max_length=100) # name of the product
	origin = models.CharField(max_length=100) # origin for catagorizing
	description = models.CharField(max_length=100) 
	wig = models.CharField(max_length=100) # color of wig
	price = models.DecimalField(max_digits=10, decimal_places=3) # in $
	image = models.ImageField(upload_to='media', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('creature-detail', kwargs={'creature_id':self.id})

	def __str__(self):
		return " #%d %s-%s wig"%(self.id,self.name,self.wig)


class Cart(models.Model):
	date = models.DateField(auto_now_add=True, )
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="cart")
	creatures = models.ManyToManyField(Creature, through='CartItem')

class CartItem(models.Model):
	cart= models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
	creature = models.ForeignKey(Creature, on_delete=models.CASCADE, related_name="cart_items")
	quantity = models.PositiveIntegerField()


