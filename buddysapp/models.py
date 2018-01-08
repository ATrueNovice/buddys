from django.db import models
from django.contrib.auth.models import User

class Dispensary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dispensary')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to= 'dispensary_logo/', blank=False)

    def __str__(self):
        return self.name

#Objects for each customer Object
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    # Add Tags for usage in this space
        #Optional Checkbox with the size and price variants

class Products(models.Model):
    dispensary = models.ForeignKey(Dispensary)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product_images/', blank=True)
    sizes = models.CharField(max_length=100, default='Size')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
