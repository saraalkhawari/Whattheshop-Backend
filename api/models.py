from django.db import models


class Creature(models.Model):
	name = models.CharField(max_length=100) # name of the product
	origion = models.CharField(max_length=100) # origion for catagorizing
	decreption = models.CharField(max_length=100) 
	wig = models.CharField(max_length=100) # color of wig
	price = models.DecimalField(max_digits=10, decimal_places=3) # in $
	image = models.ImageField(upload_to='media')



	def __str__(self):
		return self.name