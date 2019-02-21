# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class ContactNumber(models.Model):
    number = models.CharField(max_length=255)
admin.site.register(ContactNumber)

class Signup(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,blank=True, null=True)
    number = models.ForeignKey(ContactNumber)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)
admin.site.register(Signup)

<<<<<<< HEAD
=======

class Sample(models.Model):
    name = models.CharField(max_length=255)

>>>>>>> a5228e9d7e7b72e871f71e74f25c41574b807dc2
class Simple(models.Model):
    number = models.IntegerField()
