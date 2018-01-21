from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

class Product(models.Model):
    dispensary = models.ForeignKey(Dispensary)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product_images/', blank=False)
    CATEGORIES = (
    ('Usage', (
        ('new','New Strains'),
        ('headache', 'Headache'),
        ('insomnia', 'Insomnia'),
        ('social', 'Fun With Friends'),
        ('first_time', 'First Timers'),
        ('women','Menstrual Crams & Pains'),
        ('body', 'Body Pains'),
        ('stress', 'Stress and Tension'),
        ('creative', 'Creativity'),
        ('productive', 'Productivity'),
        ('food', 'Edibles'),
        ('oils', 'Oils & Dabs'),
        ('acc', 'Accessories'),
            )),
        )
    primary_usage = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    secondary_usage = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    SIZE = (
    ('Sizes',(
        ('half', 'Half Gram'),
        ('gram', 'Gram'),
        ('eighth', 'Eighth Ounce'),
        ('quarter', 'Quarter Ounce'),
        ('half', 'Half Ounce'),
        ('oz', 'Ounce'),
    )),
    )
    sizes = models.CharField(max_length=100, choices=SIZE, blank = True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    PICKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES = (
    (PICKING, "Your Order Is Being Picked Right Off The Plant!"),
    (READY, "Picked, Weighed, And Ready For Delivery."),
    (ONTHEWAY, "The Best Bud Is Heading Straight To Your Door."),
    (DELIVERED, "Delivered"),
    )

    customer = models.ForeignKey(Customer)
    dispensary = models.ForeignKey(Dispensary)
    driver = models.ForeignKey(Driver, blank = True, null = True)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices = STATUS_CHOICES)
    created_at = models.DateTimeField(default = timezone.now)
    picked_at = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)
