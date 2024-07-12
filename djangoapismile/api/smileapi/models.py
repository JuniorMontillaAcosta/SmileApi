from django.db import models
from django.conf import settings

# Create your models here.

class HeartRate(models.Model):
	class Meta:
		verbose_name = 'Heart Rate'
		verbose_name_plural = 'Heart Rates'

	user   	 	= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	bpm 		= models.CharField(max_length=20, verbose_name='BPM')
	intent		= models.CharField(max_length=20, verbose_name='intenciti')
	content		= models.CharField(max_length=120, verbose_name='content')
	updated     = models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0} BPM".format(self.bpm)