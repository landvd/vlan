from django.db import models

class table(models.Model):
	onuid = models.CharField(max_length=255)
	onumac = models.CharField(max_length=255)
	onuaddress = models.CharField(max_length=255)
	onuvlan = models.CharField(max_length=4)
	eocmac = models.CharField(max_length=255)
	eocip = models.CharField(max_length=255)
	date = models.DateTimeField()
	author = models.CharField(max_length=255)