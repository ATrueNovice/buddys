from django.contrib import admin

# Register your models here.
from buddysapp.models import Dispensary, Customer, Driver, Products

#Imports the classes that were made in the models.py file  for sign up
admin.site.register(Dispensary)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Products)
