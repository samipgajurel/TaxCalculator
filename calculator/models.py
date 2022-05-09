from django.db import models


# Create your models here.
class Calculator(models.Model):
    monthlySalary = models.FloatField(db_column="monthly_salary")
    housingRentAllowance = models.FloatField(db_column="housing_rent_allowance")
    costOfLivingAllowance = models.FloatField(db_column="cost_living_allowance")
    transportationAllowance = models.FloatField(db_column="transportation_allowance")
    bonus = models.FloatField(db_column="bonus_amount")
    overTimePayment = models.FloatField(db_column="over_time_payment")
    medicalInsurance = models.FloatField(db_column="medical_insurance")
    lifeInsurance = models.FloatField(db_column="life_insurance")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        db_table = "calculator"




