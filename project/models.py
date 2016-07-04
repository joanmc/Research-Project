# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Final(models.Model):
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='Room')  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=30, blank=True, null=True)  # Field name made lowercase.
    avgnumwificonn = models.FloatField(db_column='AvgNumWifiConn', blank=True, null=True)  # Field name made lowercase.
    groundtruth = models.FloatField(db_column='GroundTruth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Final'
        unique_together = (('datetime', 'room'),)


class Modules(models.Model):
    moduletitle = models.CharField(db_column='ModuleTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numberregistered = models.IntegerField(db_column='NumberRegistered', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Modules'


class Rooms(models.Model):
    room = models.CharField(db_column='Room', primary_key=True, max_length=10)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.

    class Meta:
        db_table = 'Rooms'
