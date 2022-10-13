from rest_framework import serializers
from wallet.models import Customer, Wallet, Account, Card, Transaction, Loan, Receipt, Notification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","age","email")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("wallet_name","customer","currency","balance")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_name","account_number","account_type","account_balance")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_name","card_number","card_type")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("amount","transaction_type","transaction_cost","origin_account","destination_account")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("amount","interest_rate","borrow_date_and_time","payment_due_date")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("receipt_type","date_issued","total_amount")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("recipient","message","date_time")