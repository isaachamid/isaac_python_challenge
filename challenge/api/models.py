from django.db import models

class Device(models.Model):
	myid = models.CharField(max_length=100)
	deviceModel = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	note = models.CharField(max_length=300)
	serial = models.CharField(max_length=100)
