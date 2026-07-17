from django.db import models
from hotels.models import Hotel
from django.contrib.auth.models import User


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()

    check_in = models.DateField()
    check_out = models.DateField()

    guests = models.IntegerField()

    booked_on = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.guest_name} - {self.hotel.name}"
# Create your models here.
