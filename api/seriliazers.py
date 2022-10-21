from .models import *
from rest_framework import serializers

class PriceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PriceOption
        fields= ['name','freekm','dbp','dap','tmf']

class CustomerSerilizer(serializers.ModelSerializer):
    total=PriceSerilizer()
    class Meta:
        model = Customer
        fields= ['name','number','origin','destination','distance','total_price','total']

