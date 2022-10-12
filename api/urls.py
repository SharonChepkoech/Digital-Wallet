from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewsets


router=routers.DefaultRouter()
router.register(r'customers',CustomerViewsets)
urlpatterns=[
    path('',include(router.urls)),
]