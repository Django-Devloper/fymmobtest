from django.contrib.auth.models import User
from django.db import models
import datetime

now = datetime.datetime.now()
dt=now.strftime("%A")


# Create your models here.
class StatusChoice(models.Model):
   status_choice= models.CharField(max_length=20)

   def __str__(self):
       return self.status_choice

class PriceOption(models.Model):
    name=models.CharField(max_length=100)
    freekm=models.FloatField(max_length=10)
    dbp=models.FloatField(max_length=10)
    dap=models.FloatField(max_length=10)
    tmf=models.FloatField(max_length=10)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

def farechoice():
    try:
        today_price = PriceOption.objects.get(name__icontains=dt)  # it will return auto price as per day name
        return today_price
    except:
        try:
            active = PriceOption.objects.get(isactive=True) #it will return manually active price
        except:
            active = PriceOption.objects.get(id=1) # it will return default price option
        return active


class Trips(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    starttime=models.DateTimeField(auto_now=True)
    endtime=models.DateTimeField(auto_now=True)
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    status=models.ForeignKey(StatusChoice,on_delete=models.CASCADE)
    distance=models.PositiveSmallIntegerField(default=10)
    fare_details=models.ForeignKey(PriceOption,on_delete=models.CASCADE,default=farechoice)

    def duration(self):
        duration =self.starttime-self.endtime
        return duration


    @property
    def total_fare(self):
        D = self.distance-self.fare_details.freekm
        total_fare = self.fare_details.dbp+(D*self.fare_details.dap)*self.fare_details.tmf
        return total_fare