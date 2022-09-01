from django.urls import path
from .views import create_account, register_customer
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
    path("add reward/", send_notification, name="reward"),
    path("add receipt/", send_notification, name="receipt"),
    path("add third party/", send_notification, name="third party"),
    path("make transaction/", send_notification, name="transaction"),
    path("add wallet/", send_notification, name="wallet"),


]