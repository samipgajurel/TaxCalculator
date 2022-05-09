from django.shortcuts import render
from django.http import HttpResponse
from .apps import TaxinfoConfig
# Create your views here.
from .models import Taxinfo


def displayinfo(request):
    records_single = TaxinfoConfig.taxInfoSingle
    records_married = TaxinfoConfig.taxInfoMarried
    sum_single = 0
    sum_married = 0
    for i in range(len(records_single)):
        sum_single+= records_single[i].taxableIncome
        sum_married+=records_married[i].taxableIncome
    sum_single = Taxinfo.commaFormatted(sum_single)
    sum_married=Taxinfo.commaFormatted(sum_married)
    records = {
        "single":records_single,
        "married":records_married,
        "sum_single":sum_single,
        "sum_married":sum_married
    }

    return render(request, 'TaxInfo.html', {"records": records})
    # return HttpResponse(result)

