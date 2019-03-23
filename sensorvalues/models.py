# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
#Creating a class for sensor values of plant 1
class weather(models.Model):
        temperature = models.CharField(max_length=250)
	humidity = models.CharField(max_length=250)
	waterlevel = models.CharField(max_length=250)
	rain = models.CharField(max_length=250)
	day = models.CharField(max_length=10,null=True)
	year = models.CharField(max_length=10,null=True)
	month = models.CharField(max_length=10,null=True)
	hour = models.CharField(max_length=10,null=True)
	minute = models.CharField(max_length=10,null=True)
class plantid(models.Model):
    pid = models.IntegerField(primary_key = True)
    latitude = models.CharField(max_length = 10,null=True)
    longitude = models.CharField(max_length = 10,null=True)
    def __str__(self):
        return str(self.pid)
class Plant(models.Model):
    pid = models.ForeignKey(plantid,null=True)
    moisture = models.CharField(max_length = 8,null=True)
    ph = models.CharField(max_length = 8,null=True)


       

