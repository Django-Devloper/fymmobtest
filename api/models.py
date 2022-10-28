from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class City(models.Model):
    city=models.CharField(max_length=100)

    def __str__(self):
        return  self.city
class StatusChoice(models.Model):
   status_choice= models.CharField(max_length=20)

   def __str__(self):
       return self.status_choice

class PriceOption(models.Model):
    name=models.CharField(max_length=100)
    freekm=models.CharField(max_length=100)
    dbp=models.FloatField(max_length=10)
    dap=models.FloatField(max_length=10)
    tmf=models.FloatField(max_length=10)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

def activefare():
    fare=PriceOption.objects.get(isactive=True)
    return fare

class Trips(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    starttime=models.DateTimeField(auto_now=True)
    endtime=models.DateTimeField(auto_now=True)
    origin=models.ForeignKey(City,on_delete=models.CASCADE,related_name='origin')
    destination=models.ForeignKey(City,on_delete=models.CASCADE,related_name='destination')
    status=models.ForeignKey(StatusChoice,on_delete=models.CASCADE)
    distance=models.PositiveSmallIntegerField(default=10)
    fare_details=models.ForeignKey(PriceOption,on_delete=models.CASCADE,default=activefare)

    def duration(self):
        duration =self.starttime-self.endtime
        return duration


    def total_price(self):
        D = self.distance-int(self.fare_details.freekm)
        total = self.fare_details.dbp+(D*self.fare_details.dap)*self.fare_details.tmf
        return total