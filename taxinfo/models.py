from django.db import models

class Taxinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    maritalStatus = models.CharField(db_column='maritalStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxableIncome = models.IntegerField(db_column='taxableIncome', blank=True, null=True)  # Field name made lowercase.
    taxRate = models.IntegerField(db_column='taxRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxinfo'

    @property
    def taxableIncomeStr(self):
        return Taxinfo.commaFormatted(self.taxableIncome)

    @staticmethod
    def commaFormatted(num):
        if num < 1000:
            return str(num)
        result = ""
        rem = num % 1000
        result = str(rem).zfill(3) + result
        num = num // 1000
        result = f",{result}"
        while num > 99:
            rem = num % 100
            result = "," + str(rem).zfill(2) + result
            num = num // 100
        result = f"{str(num)}{result}"
        return result

