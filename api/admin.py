from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(StatusChoice)
admin.site.register(City)

@admin.register(PriceOption)
class PriceOptionAdmin(admin.ModelAdmin):
    list_display = ['name','freekm', 'dbp', 'dap', 'tmf','isactive']


@admin.register(Trips)
class PriceOptionAdmin(admin.ModelAdmin):
    readonly_fields=('fare_details',)

    list_display = ['user','starttime', 'endtime', 'origin', 'destination','status','distance']
