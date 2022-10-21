from django.db import models

# Create your models here.


class PriceOption(models.Model):
    name=models.CharField(max_length=100)
    freekm=models.CharField(max_length=100)
    dbp=models.FloatField(max_length=10)
    dap=models.FloatField(max_length=10)
    tmf=models.FloatField(max_length=10)


class Customer(models.Model):
    name=models.CharField(max_length=100)
    number=models.PositiveBigIntegerField()
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    distance=models.FloatField(blank=True,null=True)
    total=models.ForeignKey(PriceOption,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    @property
    def total_price(self):
        D = self.distance-int(self.total.freekm)
        return (self.total.dbp+(D*self.total.dap))*self.total.tmf

