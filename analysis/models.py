from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username

class County(models.Model):
	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()

	class Meta:
		verbose_name_plural = "Counties" 

class Incidents(models.Model):
	list_of_at = models.CharField(max_length=254)
	f2 = models.CharField(max_length=254)
	x = models.FloatField()
	y = models.FloatField()
	casulties = models.IntegerField()
	geom = models.MultiPointField(srid=4326)
	objects = models.GeoManager()

	def __str__(self):
		return self.list_of_at

	class Meta:
		verbose_name_plural = "Incidents"
