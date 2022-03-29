from django.db import models


# Create your models here.
# class TaxInfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     maritalStatus = models.CharField(max_length=2)
#     taxableIncome = models.IntegerField()
#     taxRate = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = "taxinfo"
#
class Taxinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    maritalStatus = models.CharField(db_column='maritalStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxableIncome = models.IntegerField(db_column='taxableIncome', blank=True, null=True)  # Field name made lowercase.
    taxRate = models.IntegerField(db_column='taxRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxinfo'


