from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.


class Reservation(models.Model):
    """
    Stores a single reservation entry related to :model: `auth.User`.
    
    Attributes:
        user (foreignkey): reference to the user in the user builtin model.
        name: name of the user whow made the booking.
        date: the date of the booking.
        time: time of the booking.
        email: email address to contact.
        notes: optional field to enter any necessary notes.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resev_user")
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)# https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.DateField
    time = models.TimeField(default=timezone.now)
    email = models.EmailField(max_length=200)
    notes = models.TextField(blank=True, null=True)

    class Meta():
        """
        Meta data for the model.
        Order the felds from newest to oldest.
        """
        ordering = ["-date"]

    def __str__(self):
        """
        Magic method represents the instance as string.
        """
        return (f"** Dear {self.name} your booking on {self.date}, "
                f"at {self.time}, is Confirmed! **")
        
