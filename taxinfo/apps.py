from django.apps import AppConfig
from .models import Taxinfo



class TaxinfoConfig(AppConfig):
    name = 'taxinfo'
    taxInfoMarried = Taxinfo.objects.filter(maritalStatus='M')
    taxInfoSingle = Taxinfo.objects.filter(maritalStatus='S')


