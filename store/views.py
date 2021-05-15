from django.shortcuts import render, HttpResponse, redirect
from store.models import Medicine, Sold
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, AddMedicineForm, SellMedicineForm
from .filters import MedicineFilter, SoldFilter

# Create your views here.
@login_required(login_url='Login')
def index(request):
    return render(request, 'store/index.html')


@login_required(login_url='Login')
def about(request):
    return render(request, 'store/about.html')


@login_required(login_url='Login')
def addmedicine(request):
    if request.method == "POST":
        fm = AddMedicineForm(request.POST)
        if fm.is_valid():
            cmp = fm.cleaned_data['company_name']
            med = fm.cleaned_data['medicine_name']
            mfg = fm.cleaned_data['mfg_date']
            exp = fm.cleaned_data['exp_date']
            prc = fm.cleaned_data['price']
            stc = fm.cleaned_data['stock']
            reg = Medicine(company_name=cmp, medicine_name=med, mfg_date=mfg, exp_date=exp, price=prc, stock=stc)
            reg.save()
            fm = AddMedicineForm()
            at = "Successfull! Data Added Successfully"
            return render(request, 'store/addmedicine.html', {"status": at, "form": fm})
    else:
        fm = AddMedicineForm()

    return render(request, 'store/addmedicine.html', {'form':fm})


@login_required(login_url='Login')
def inventory(request):
    tdata = Medicine.objects.all()

    myFilter = MedicineFilter(request.GET, queryset=tdata)
    tdata = myFilter.qs
    

    return render(request, 'store/inventory.html', {"messages": tdata, "myFilter": myFilter})


@login_required(login_url='Login')
def update_med(request, id):
    if request.method == "POST":
        pi = Medicine.objects.get(pk=id)
        fm = AddMedicineForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('Inventory')
    else:
        pi = Medicine.objects.get(pk=id)
        fm = AddMedicineForm(instance=pi)     
    return render(request, 'store/update.html', {"form":fm})


@login_required(login_url='Login')
def delete_med(request, id):
    pi = Medicine.objects.get(pk=id)
    if request.method == "POST":
        pi.delete()
        return redirect('Inventory')

    return render(request, 'store/deletemedicine.html', {"med": pi})


@login_required(login_url='Login')
def delete_rec(request, id):
    pi = Sold.objects.get(pk=id)
    if request.method == "POST":
        pi.delete()
        return redirect('Records')

    return render(request, 'store/deleterecords.html', {"rec": pi})


@login_required(login_url='Login')
def sellmedicine(request, id):
    if request.method == "POST":
        pi = Medicine.objects.get(pk=id)
        fm = SellMedicineForm(request.POST, instance=pi)
        if fm.is_valid():
            cmp = fm.cleaned_data['company_name']
            med = fm.cleaned_data['medicine_name']
            mfg = fm.cleaned_data['mfg_date']
            exp = fm.cleaned_data['exp_date']
            prc = fm.cleaned_data['price']
            cus = fm.cleaned_data['customer']
            phn = fm.cleaned_data['phone']
            qty = fm.cleaned_data['quantity']
            amt = fm.cleaned_data['amount']
            pdt = fm.cleaned_data['purchase_date']
            reg = Sold(company_name=cmp, medicine_name=med, mfg_date=mfg, exp_date=exp, price=prc, customer=cus, phone=phn, quantity=qty, amount=amt, purchase_date=pdt)
            reg.save()
            item = int(qty)
            pi.stock -= item
            pi.save()
            return redirect('Inventory')
    else:
        pi = Medicine.objects.get(pk=id)
        fm = SellMedicineForm(instance=pi)
    return render(request, 'store/sellmedicine.html', {"form": fm})


@login_required(login_url='Login')
def records(request):
    tdata = Sold.objects.all()

    myFilter = SoldFilter(request.GET, queryset=tdata)
    tdata = myFilter.qs

    return render(request, 'store/records.html', {"messages": tdata, "myFilter": myFilter})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'store/index.html')
        else:
            msg = "Username or Password is incorrect"
            return render(request, 'store/login.html', {"message":msg})

    return render(request, 'store/login.html')


def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Successfully created!")
            return redirect('Login')

    context = {"form":form}
    return render(request, 'store/signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Login')

