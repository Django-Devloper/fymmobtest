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
    status=serializers.ReadOnlyField(source="status.status_choice")
    class Meta:
        model = Trips
        fields= ['id','origin','destination','duration','starttime','endtime','status','distance','total_fare','user','fare_details']

