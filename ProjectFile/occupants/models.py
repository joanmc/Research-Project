# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Rooms(models.Model):
    room = models.CharField(db_column='Room', primary_key=True, max_length=10)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=30, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Rooms'
