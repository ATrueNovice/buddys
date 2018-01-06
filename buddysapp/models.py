from django.db import models
from django.contrib.auth.models import User

class Dispensary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dispensary')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='dispensary_logo/', blank=False)


    #def __str__(self):
    #    return self.name
