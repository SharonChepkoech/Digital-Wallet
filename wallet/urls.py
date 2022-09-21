from django.urls import path
from .views import add_receipt, add_reward, add_third_party, add_wallet, create_account, make_transaction, register_customer
from .views import add_card
from .views import add_currency
from .views import request_loan
from .views import send_notification

urlpatterns =[
    path("register/", register_customer, name="registration"),
    path("add card/", add_card, name="card addition"),
    path("add currency/", add_currency, name = "currency addition"),
    path("create account/", create_account, name="account creation"),
    path("request loan/", request_loan, name="loan request"),
    path("send notification/", send_notification, name="notification"),
    path("add reward/", add_receipt, name="reward"),
    path("add receipt/", add_reward, name="receipt"),
    path("add third party/", add_third_party, name="third party"),
    path("make transaction/", make_transaction, name="transaction"),
    path("add wallet/", add_wallet, name="wallet"),
]