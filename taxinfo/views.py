from django.shortcuts import render
from django.http import HttpResponse
from .models import Taxinfo
# Create your views here.
def displayinfo(request):
    records = Taxinfo.objects.all()
    result = 'Printing all TaxInfo entries in the DB : <br>'
    for record in records:
        result += f"{record.maritalStatus}\t{record.taxableIncome}\t{record.taxRate}<br>"
    return render(request, 'TaxInfo.html', {"records": records})
    # return HttpResponse(result)

