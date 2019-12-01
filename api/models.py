from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Creature(models.Model):
	name = models.CharField(max_length=120)
	origin = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	image = models.ImageField(upload_to='creature_logos', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('creature-detail', kwargs={'creature_id':self.id})
