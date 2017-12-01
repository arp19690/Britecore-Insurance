# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class RiskTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = True
        db_table = 'risk_types'


class RiskTypeFields(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    risk_type = models.ForeignKey(RiskTypes)
    display_name = models.CharField(max_length=35, default=None)
    field_name = models.CharField(max_length=25)
    field_type = models.CharField(max_length=10, choices=(('text', 'Text'),
                                                          ('number', 'Number'),
                                                          ('date', 'Date'),
                                                          ('enum', 'Enum')))

    class Meta:
        managed = True
        db_table = 'risk_type_fields'
        unique_together = (('risk_type', 'field_name'),)
