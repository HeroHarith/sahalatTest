from django.db import models
from django.contrib.auth.models import User
# Create your models here.

types = [
    
	(0, "customer"),
 (1, "driver")   
]

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=8)
	ac_type = models.IntegerField(choices=types)
	address = models.CharField(max_length=200)

	def __name__(self):
		self.user.get_full_name()
	



class Car(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=150)
	number = models.CharField(max_length=10)
	def __str__(self):
		return self.name


