# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Groundtruth(models.Model):
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='Room')  # Field name made lowercase.
    binaryestimate = models.IntegerField(db_column='BinaryEstimate', blank=True, null=True)  # Field name made lowercase.
    percentageestimate = models.FloatField(db_column='PercentageEstimate', blank=True, null=True)  # Field name made lowercase.
    groundtruthid = models.AutoField(db_column='GroundTruthId', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'GroundTruth'


class Modules(models.Model):
    modulename = models.CharField(db_column='ModuleName', primary_key=True, max_length=30)  # Field name made lowercase.
    numreg = models.IntegerField(db_column='NumReg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Modules'


class Rooms(models.Model):
    room = models.CharField(db_column='Room', primary_key=True, max_length=10)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=30, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Rooms'


class Timemodule(models.Model):
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    room = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='Room')  # Field name made lowercase.
    module = models.ForeignKey(Modules, models.DO_NOTHING, db_column='Module')  # Field name made lowercase.
    timemoduleid = models.AutoField(db_column='TimeModuleId', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TimeModule'


class Wifilogdata(models.Model):
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    room = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='Room')  # Field name made lowercase.
    associated = models.IntegerField(db_column='Associated', blank=True, null=True)  # Field name made lowercase.
    authenticated = models.IntegerField(db_column='Authenticated', blank=True, null=True)  # Field name made lowercase.
    wifilogdataid = models.AutoField(db_column='WiFiLogDataId', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'WiFiLogData'