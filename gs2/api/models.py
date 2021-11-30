# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 100)
    roll = models.IntegerField()
    city = models.CharField(max_length= 100)
    