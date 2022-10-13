from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewsets, AccountViewset, CardViewset, LoanViewset, NotificationViewset, ReceiptViewset, TransactionViewset, WalletViewset


router=routers.DefaultRouter()
router.register(r'customers',CustomerViewsets)
router.register(r"wallets",WalletViewset)
router.register(r"accounts",AccountViewset)
router.register(r"cards",CardViewset)
router.register(r"transactions",TransactionViewset)
router.register(r"loans",LoanViewset)
router.register(r"receipts",ReceiptViewset)
router.register(r"notifications",NotificationViewset)

urlpatterns=[
    path('',include(router.urls)),
    
]