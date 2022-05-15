# Generated by Django 3.1.7 on 2022-05-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='bonus',
            field=models.FloatField(db_column='bonus_amount'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='costOfLivingAllowance',
            field=models.FloatField(db_column='cost_living_allowance'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='housingRentAllowance',
            field=models.FloatField(db_column='housing_rent_allowance'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='lifeInsurance',
            field=models.FloatField(db_column='life_insurance'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='medicalInsurance',
            field=models.FloatField(db_column='medical_insurance'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='monthlySalary',
            field=models.FloatField(db_column='monthly_salary'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='overTimePayment',
            field=models.FloatField(db_column='over_time_payment'),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='transportationAllowance',
            field=models.FloatField(db_column='transportation_allowance'),
        ),
    ]