from rest_framework import serializers
from wallet.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","age","email")