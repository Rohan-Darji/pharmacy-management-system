import django_filters

from .models import *

class MedicineFilter(django_filters.FilterSet):
    class Meta:
        model = Medicine
        fields = '__all__'
        exclude = ['mfg_date', 'exp_date', 'price', 'stock']


class SoldFilter(django_filters.FilterSet):
    class Meta:
        model = Sold
        fields = '__all__'
        exclude = ['company_name', 'mfg_date', 'exp_date', 'price', 'quantity', 'amount']