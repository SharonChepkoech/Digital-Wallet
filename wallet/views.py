from urllib import request
from django.shortcuts import render, redirect
from .import models
from .import forms

# Create your views here.


def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def list_customers(request):
    customers = models.Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers": customers})

def customer_profile(request,id):
    customer = models.Customer.objects.get(id = id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_customer(request,id):
    customer = models.Customer.objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST,instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form =forms.CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer.html",{"form":form})



def add_card(request):
    if request.method == "POST":
        form = forms.CardAdditionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CardAdditionForm()
    return render(request,"wallet/add_card.html",{"form":form})

def list_cards(request):
    customers = models.Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers": customers})



def add_currency(request):
    if request.method == "POST":
        form = forms.CurrencyAdditionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CurrencyAdditionForm()
    return render(request,"wallet/add_currency.html",{"form":form})
    
    
def create_account(request):
    if request.method == "POST":
        form = forms.AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AccountCreationForm()
    return render(request,"wallet/create_account.html",{"form":form})
  
    
def request_loan(request):
    if request.method == "POST":
        form = forms.LoanRequestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.LoanRequestForm()
    return render(request,"wallet/request_loan.html",{"form":form})
   

def send_notification(request):
     if request.method == "POST":
        form = forms.SendNotification(request.POST)
        if form.is_valid():
            form.save()
     else:
        form = forms.SendNotification()
     return render(request,"wallet/send_notification.html",{"form":form})

def add_receipt(request):
    if request.method == "POST":
        form = forms.AddReceipt(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AddReceipt()
    return render(request,"wallet/add_receipt.html",{"form":form})

def add_reward(request):
    if request.method == "POST":
        form = forms.AddReward(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AddReward()
    return render(request,"wallet/add_reward.html",{"form":form})

def add_third_party(request): 
    if request.method == "POST":
        form = forms.ThirdParty(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ThirdParty()
    return render(request,"wallet/add_third_party.html",{"form":form})

   
def make_transaction(request):
    if request.method == "POST":
        form = forms.MakeTransaction(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.MakeTransaction()
    return render(request,"wallet/make_transaction.html",{"form":form})

   
def add_wallet(request):
    if request.method == "POST":
        form = forms.AddWallet(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AddWallet()
    return render(request,"wallet/add_wallet.html",{"form":form})

