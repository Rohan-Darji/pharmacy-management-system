from django.contrib import admin
from django.contrib.auth.models import User

admin.site.site_header="Pharmacy Management System"

class MedicineAdmin(admin.ModelAdmin):
    list_display = ["id", "company_name", "medicine_name", "mfg_date", "exp_date", "price", "stock"]
    search_fields = ["medicine_name"]

class SoldAdmin(admin.ModelAdmin):
    list_display = ["id", "company_name", "medicine_name", "mfg_date", "exp_date", "price", "customer", "phone", "quantity", "amount", "purchase_date"]
    search_fields = ["medicine_name", "customer"]

# Register your models here.
from .models import Medicine
from .models import Sold



admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Sold, SoldAdmin)

