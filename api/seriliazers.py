from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','date_joined']


class PriceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PriceOption
        fields= ['name','freekm','dbp','dap','tmf']

class CustomerSerilizer(serializers.ModelSerializer):
    fare_details=PriceSerilizer()
    user=UserSerilizer()
    origin=serializers.ReadOnlyField(source="origin.city")
    destination=serializers.ReadOnlyField(source="destination.city")
    class Meta:
        model = Trips
        fields= ['user','starttime','endtime','duration','origin','destination','status','distance','total_price','fare_details']

