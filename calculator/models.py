from django.db import models


# Create your models here.
class Calculator(models.Model):
    monthlySalary = models.FloatField()
    housingRentAllowance = models.FloatField()
    costOfLivingAllowance = models.FloatField()
    transportationAllowance = models.FloatField()
    bonus = models.FloatField()
    overTimePayment = models.FloatField()
    medicalInsurance = models.FloatField()
    lifeInsurance = models.FloatField()

    class Meta:
        db_table = "calculator"

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
