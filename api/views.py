from rest_framework import viewsets
from wallet.models import Customer
from .serializer import CustomerSerializer

# Create your views here.
class CustomerViewsets(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
# Create your views here.
