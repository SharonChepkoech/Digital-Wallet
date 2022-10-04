from django.urls import path
from .import views 

urlpatterns =[
    path("register/", views.register_customer, name="registration"),
    path("customers/",views.list_customers, name = "list customers"),
    path("customers/<int:id>/",views.customer_profile,name ="customer_profile"),
    path("customers/edit/<int:id>/",views.edit_customer,name="edit_customer"),
    path("add card/", views.add_card, name="card addition"),
    path("add currency/", views.add_currency, name = "currency addition"),
    path("create account/", views.create_account, name="account creation"),
    path("request loan/", views.request_loan, name="loan request"),
    path("send notification/", views.send_notification, name="notification"),
    path("add reward/", views.add_receipt, name="reward"),
    path("add receipt/", views.add_reward, name="receipt"),
    path("add third party/", views.add_third_party, name="third party"),
    path("make transaction/", views.make_transaction, name="transaction"),
    path("add wallet/", views.add_wallet, name="wallet"),
]