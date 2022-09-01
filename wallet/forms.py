from dataclasses import field
from pyexpat import model
from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class CardAdditionForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
class CurrencyAdditionForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"
class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"
class SendNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"
class AddReceipt(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"
class AddReward(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"
class AddThirdParty(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = "__all__"
class MakeTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
class AddWallet(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"