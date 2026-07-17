from django.db import models

class Hotel(models.Model):
    HOTEL_TYPES = [
        ('Luxury', 'Luxury'),
        ('Resort', 'Resort'),
        ('Business', 'Business'),
        ('Budget', 'Budget'),
    ]

    name = models.CharField(max_length=200)
    hotel_type = models.CharField(max_length=20, choices=HOTEL_TYPES)
    city = models.CharField(max_length=100)
    address = models.TextField()

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='hotels/')

    rating = models.FloatField(default=5.0)

    total_rooms = models.PositiveIntegerField(default=10)

    available_rooms = models.PositiveIntegerField(default=10)

    wifi = models.BooleanField(default=True)
    parking = models.BooleanField(default=True)
    restaurant = models.BooleanField(default=True)
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name