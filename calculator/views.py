from calculator.service import calculate_tax
from calculator.models import Calculator
from django.shortcuts import render
from taxinfo.models import Taxinfo

from django.http import HttpResponse
# Create your views here.

def calculator_page(request):
    return render(request, 'TaxCalculator.html')


def parse_float(value):
    if value == "":
        return 0
    else:
        return float(value)

def incomeTax(request):
    if request.method =="POST":
        params = request.POST
    elif request.method == "GET":
        params = request.GET
    print(params)
    keys = ['monthlySalary', 'housingRentAllowance','costOfLivingAllowance'
        ,'transportationAllowance','bonus','overTimePayment','medicalInsurance','lifeInsurance']
    data={}
    for key in keys:
        print(key)
        data[key] = parse_float(params[key])
    print(data)
    model = Calculator(**data)
    marital_status = params["maritalStatus"]
    tax= calculate_tax(model,marital_status.upper())
    data['tax'] = Taxinfo.commaFormatted(int(tax))
    return render(request, 'TaxCalculator.html', data)

