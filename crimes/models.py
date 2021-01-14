# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Murder_victim_age_sex(models.Model):
#     Area_Name = models.TextField()
#     Year = models.TextField()
#     Group_Name = models.TextField()
#     Sub_Group_Name = models.TextField()
#     Loss_of_Property_1_10_Crores = models.TextField()
#     Loss_of_Property_10_25_Crores = models.TextField()
#     Loss_of_Property_25_50_Crores = models.TextField()
#     Loss_of_Property_50_100_Crores = models.TextField()
#     Loss_of_Property_Above_100_Crores = models.TextField()
#
#     def __str__(self):
#         return self.Area_Name


class AgainstWomen(models.Model):
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
