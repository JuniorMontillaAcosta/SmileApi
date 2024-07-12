from django.db import models
from django.conf import settings

# Create your models here.
class UserProfModel(models.Model):
	CHOICES     	=  [('doctor','doctor'), ('fathers','fathers'), ('teachers','teachers')]
	username_prof 	=  models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
	prof 			=  models.CharField(choices=CHOICES, max_length=45)

	def __str__(self):
		return '{0}'.format(self.username_prof)