from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.


# class Reservation(models.Model):
class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resev_user")
    name = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    email = models.EmailField(max_length=50)
    notes = models.TextField()

    class Meta():
        ordering = ["-date"]

    def __str__(self):

        return f"Dear {self.name} your booking on {self.date} at {self.time} confirmed"
        #return f"reservation for {self.name}"
