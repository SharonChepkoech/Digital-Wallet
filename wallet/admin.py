import email
from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_fields=("first_name","last_name")

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_name","balance", "wallet")
    search_fields = ("account_name",)   

class CurenecyAdmin(admin.ModelAdmin):
    list_display =("symbol","country_of_origin","name")
    search_fields = ("symbol",) 

class WalletAdmin(admin.ModelAdmin):
    list_display =("wallet_name","customer","currency",)
    search_fields = ("wallet_name",) 

class TransactionAdmin(admin.ModelAdmin):
    list_display =("transaction_type","origin_account","third_party","transaction_amount")
    search_fields = ("transaction_type","origin_account",) 

class CardAdmin(admin.ModelAdmin):
    list_display =("card_name","card_number","issuer",)
    search_fields = ("card_name",) 

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display =("full_name","email","transaction_cost","is_active")
    search_fields = ("full_name",) 

class NotificationAdmin(admin.ModelAdmin):
    list_display =("recipient","date_time",)
    search_fields = ("recipient",)

class ReceiptAdmin(admin.ModelAdmin):
    list_display =("receipt_type","receipt_date","total_amount")
    search_fields = ("receipt_type",)

class LoanAdmin(admin.ModelAdmin):
    list_display =("loan_term","amount","payment_due_date")
    search_fields = ("loan_term",)

class RewardAdmin(admin.ModelAdmin):
    list_display =("bonus","wallet","date_given")
    search_fields = ("wallet","bonus",)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurenecyAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward, RewardAdmin)


