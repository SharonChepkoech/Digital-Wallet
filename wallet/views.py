from urllib import request
from django.shortcuts import render

from wallet.models import ThirdParty
from .forms import CustomerRegistrationForm
from .forms import CardAdditionForm
from .forms import CurrencyAdditionForm
from .forms import AccountCreationForm
from .forms import LoanRequestForm
from .forms import SendNotification
from .forms import AddReceipt
from .forms import AddReward
from .forms import AddThirdParty
from .forms import MakeTransaction
from .forms import AddWallet
# Create your views here.


def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",
    {"form":form})

def add_card(request):
    form = CardAdditionForm()
    return render (request, "wallet/add_card.html",
    {"form":form})

def add_currency(request):
    form = CurrencyAdditionForm()
    return render(request, "wallet/add_currency.html",
    {"form":form})
def create_account(request):
    form = AccountCreationForm()
    return render(request, "wallet/create_account.html",
    {"form":form})
def request_loan(request):
    form = LoanRequestForm()
    return render(request, "wallet/request_loan.html",
    {"form":form})
def send_notification(request):
    form = SendNotification()
    return render(request, "wallet/send_notification.html",
    {"form":form})
def add_receipt(request):
    form = AddReceipt()
    return render(request, "wallet/add_receipt.html",
    {"form":form})
def add_reward(request):
    form = AddReward()
    return render(request, "wallet/add_reward.html",
    {"form":form})
def add_third_party(request):
    form = ThirdParty()
    return render(request, "wallet/add_third_party.html",
    {"form":form})
def make_transaction(request):
    form = MakeTransaction()
    return render(request, "wallet/make_transaction.html",
    {"form":form})
def add_wallet(request):
    form = AddWallet()
    return render(request, "wallet/add_wallet.html",
    {"form":form})
