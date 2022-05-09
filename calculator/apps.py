from django.apps import AppConfig

from taxinfo.models import Taxinfo
from .models import Calculator


class CalculatorConfig(AppConfig):
    name = 'calculator'
    taxInfoMarried = Taxinfo.objects.filter(maritalStatus='M')
    taxInfoSingle = Taxinfo.objects.filter(maritalStatus='S')



