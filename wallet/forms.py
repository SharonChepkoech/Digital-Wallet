from dataclasses import field
from pyexpat import model
from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("first_name","last_name","gender","address","age","nationality","user_id","email","phone_number","employed","occupation","marital_status","profile_picture")
        widgets = {
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "last_name":forms.TextInput(attrs={'class':"form-control"}),
            "gender":forms.Select(attrs={'class':"form-control"}),
            "address":forms.TextInput(attrs={'class':"form-control"}),
            "nationality":forms.Select(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),
            "phone_number":forms.TextInput(attrs={'class':"form-control"}),
            "employed":forms.Select(attrs={'class':"form-control"}),
            "occupation":forms.TimeInput(attrs={'class':"form-control"}),
            "marital_status":forms.Select(attrs={'class':"form-control"}),
            "profile_picture":forms.FileInput(attrs={'class':"form-control"}),
        }

class CardAdditionForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ("card_name","card_number", "card_type","expiry_date","card_status","cvv","account","issuer","signature")
        widgets = {
            "card_name":forms.TextInput(attrs={'class':"form-control"}),
            "card_number":forms.TextInput(attrs={'class':"form-control"}),
            "card_type":forms.Select(attrs={'class':"form-control"}),
            "card_status":forms.TextInput(attrs={'class':"form-control"}),
            "expiry_date":forms.TextInput(attrs={'class':"form-control"}),
            "cvv":forms.TextInput(attrs={'class':"form-control"}),
            "account":forms.Select(attrs={'class':"form-control"}),
            "account":forms.TextInput(attrs={'class':"form-control"}),
            "issuer":forms.TextInput(attrs={'class':"form-control"}),
            "signature":forms.FileInput(attrs={'class':"form-control"}),    
        }


class CurrencyAdditionForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ("name","symbol","country_of_origin")
        widgets = {
            "name":forms.Select(attrs={'class':"form-control"}),
            "symbol":forms.TextInput(attrs={'class':"form-control"}),
            "country_of_origin":forms.Select(attrs={'class':"form-control"}),
        }

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("account_number","account_name","balance")
        widgets = {
            "account_number":forms.TextInput(attrs={'placeholder': 'Account Number', 'class':"form-control"}),
            "account_name":forms.TextInput(attrs={'placeholder': 'Account Name','class':"form-control"}),
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
        }

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = fields = ("amount","wallet","interest_rate","guarantee","borrow_date_and_time","payment_due_date","loan_balance","loan_term","loan_status","duration")
        widgets ={
             "amount":forms.TextInput(attrs={'class':"form-control"}),
             "wallet":forms.TextInput(attrs={'class':"form-control"}),
             "interest_rate":forms.TextInput(attrs={'class':"form-control"}),
             "guarantee":forms.TextInput(attrs={'class':"form-control"}),
             "borrow_date_and_time":forms.TextInput(attrs={'class':"form-control"}),
             "payment_due_date":forms.TextInput(attrs={'class':"form-control"}),
             "loan_balance":forms.TextInput(attrs={'class':"form-control"}),
             "loan_term":forms.TextInput(attrs={'class':"form-control"}),
             "loan_status":forms.TextInput(attrs={'class':"form-control"}),
             "duration":forms.TextInput(attrs={'class':"form-control"}),
             
        }
class SendNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ("recipient","message","date_time")
        widgets ={
            "recipient":forms.TextInput(attrs={'class':"form-control"}),
            "message":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
        }

class AddReceipt(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ("receipt_type","receipt_date","total_amount","receipt_file")
        widgets = {
            "receipt_type":forms.TextInput(attrs={'class':"form-control"}),
            "receipt_date":forms.TextInput(attrs={'class':"form-control"}),
            "total_amount":forms.TextInput(attrs={'class':"form-control"}),
            "receipt_file":forms.TextInput(attrs={'class':"form-control"}),
        }

class AddReward(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ("bonus","wallet","date_given")
        widgets= {
            "bonus":forms.TextInput(attrs={'class':"form-control"}),
            "wallet" :forms.TextInput(attrs={'class':"form-control"}),
            "date_given":forms.TextInput(attrs={'class':"form-control"}),
        }

class AddThirdParty(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields =  ("full_name","email","phone_number","transaction_cost","currency","is_active","account")
        widgets = {
            "full_name":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),
            "phone_number":forms.TextInput(attrs={'class':"form-control"}),
            "transacion_cost":forms.TextInput(attrs={'class':"form-control"}),
            "currency":forms.TextInput(attrs={'class':"form-control"}),
            "is_active":forms.TextInput(attrs={'class':"form-control"}),
            "account":forms.TextInput(attrs={'class':"form-control"}),
        }

class MakeTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("transaction_type","wallet","transaction_amount","transaction_date_time","receipt","origin_account","destination_account","third_party","status","transaction_cost")
        widgets = {
            "transaction_type":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_date_time":forms.TextInput(attrs={'class':"form-control"}),
            "receipt":forms.TextInput(attrs={'class':"form-control"}),
            "origin_account":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "third_party":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_cost":forms.TextInput(attrs={'class':"form-control"}),
        }        
class AddWallet(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ("wallet_name","currency","customer","balance","date_created","pin")
        widget = {
            "wallet_name":forms.TextInput(attrs={'class':"form-control"}),
            "currency":forms.TextInput(attrs={'class':"form-control"}),
            "customer":forms.TextInput(attrs={'class':"form-control"}),
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "date_created":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
        }