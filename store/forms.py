from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medicine, Sold


class SignupForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["company_name", "medicine_name", "mfg_date", "exp_date", "price", "stock"]


class SellMedicineForm(forms.ModelForm):
    class Meta:
        model = Sold
        fields = ["company_name", "medicine_name", "mfg_date", "exp_date", "price", "customer", "phone", "quantity", "amount", "purchase_date"]
