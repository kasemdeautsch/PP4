from datetime import date, time
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core .validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
values = (
    (time(9, 0), "09:00"), (time(9, 30), "09:30"),
    (time(10, 0), "10:00"), (time(10, 30), "10:30"),
    (time(11, 0), "11:00"), (time(11, 30), "11:30"),
    (time(12, 0), "12:00"), (time(12, 30), "12:30"),
    (time(17, 0), "17:00"), (time(17, 30), "17:30"),
    (time(18, 0), "18:00"), (time(18, 30), "18:30"),
    (time(19, 0), "19:00"), (time(19, 30), "19:30"),
    (time(20, 0), "20:00"), (time(20, 30), "20:30"),
)


def validate_name(value):
    """
    Validator to check if namefield contain only letters,
    raises error if it has other characters like numbers or spaces.
    """
    if not value.isalpha():
        raise ValidationError(
            _('%(value)s is not allowed!, '
              'name can contain only letters and no spaces.'),
            params={'value': value},
            )


class Reservation(models.Model):
    """
    Stores a single reservation entry related to :model: `auth.User`.
    Attributes:
        user (foreignkey): reference to the user in the user builtin model.
        name: name of the user who made the booking.
        date: the date of the booking.
        time: time of the booking, with choices to chose from
        email: email address to contact.
        notes: optional field to enter any necessary notes.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resev_user")
    name = models.CharField(max_length=200, validators=[validate_name])
    date = models.DateField(default=date.today)
    time = models.TimeField(choices=values)
    email = models.EmailField(max_length=200)
    notes = models.TextField(
        blank=True, null=True, validators=[MaxLengthValidator(600)])

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
