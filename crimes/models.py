# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Rape(models.Model):
    area = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.area

class SexualHarassment(models.Model):
    area = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.area

class AutoTheft(models.Model):
    area = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.area

class SeriousFraud(models.Model):
    area = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.area

class Murder(models.Model):
    area = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.area