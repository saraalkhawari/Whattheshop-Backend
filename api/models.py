from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# let color and image VALUE become same as color name

class Creature(models.Model):
	name = models.CharField(max_length=100) # name of the product
	origin = models.CharField(max_length=100) # origin for catagorizing
	description = models.CharField(max_length=100) 
	# wig = models.ForeignKey(Wig, on_delete=models.CASCADE, null=True, blank=True) # color of wig
	price = models.DecimalField(max_digits=10, decimal_places=3) # in $
	image = models.ImageField(upload_to='media', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('creature-detail', kwargs={'creature_id':self.id})

	def __str__(self):
		return " #%d %s"%(self.id,self.name)

class Wig(models.Model): 
	color= models.CharField(max_length=100)
	creatures = models.ManyToManyField(Creature, through='CreatureWig')

	def __str__(self):
		return self.color
	# image = models.ImageField(upload_to='media',null=True,blank=True)
	# creature = models.ForeignKey(Creature, on_delete=models.CASCADE, related_name='wigs')

# class Wigs(models.Model): 
# 	color= models.CharField(max_length=100)
# 	creature = models.ForeignKey(Creature, on_delete=models.CASCADE, related_name='wigs')
# 	image = models.ImageField(upload_to='media',null=True,blank=True)
class CreatureWig(models.Model):
	wig = models.ForeignKey(Wig, on_delete=models.CASCADE, null=True, blank=True) # color of wig
	creature = models.ForeignKey(Creature, on_delete=models.CASCADE, related_name='wigs')
	image = models.ImageField(upload_to='media',null=True,blank=True)

	def __str__(self):
		return " #%s %s"%(self.wig,self.creature)

class Cart(models.Model):
	date = models.DateField(auto_now_add=True, )
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="cart")
	creatures = models.ManyToManyField(Creature, through='CartItem')

class CartItem(models.Model):
	cart= models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
	creature = models.ForeignKey(Creature, on_delete=models.CASCADE, related_name="cart_items")
	wig = models.ForeignKey(Wig, on_delete=models.CASCADE, related_name="cart_items")
	quantity = models.PositiveIntegerField()


