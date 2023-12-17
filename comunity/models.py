from django.db import models
from django.contrib.auth.models import User

# Create your models here.
directions = [[0, "من الجامعة"], [1, "إلى الجامعة"]]
class Trip(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.TimeField()
	direction = models.IntegerField(choices=directions)
	address = models.CharField(max_length=150)
	notes = models.TextField(max_length=300)

class Order(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class Announcement(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	published_at = models.DateTimeField(auto_now=True)
	content = models.TextField(max_length=300)
