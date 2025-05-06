from django.contrib import admin
from django import forms
from .models import Reservation
import datetime


# Register your models here.
class ReservationAdminForm(forms.ModelForm):
    """
    A class to apply the choices option from Reservation Model on the time
    field With a function to clean the time field
    by applying the 'strptime' method.
    """
    time = forms.ChoiceField(
        choices=Reservation.time.field.choices, widget=forms.Select
    )


class Meta:

    model = Reservation
    fields = '__all__'


def clean_time(self):
    """
    Optaining the time field and converting to datetime.time object.
    For loop to return the correct time from choices and return it.
    """
    timestr = self.cleaned_data['time']
    tt = datetime.datetime.strptime(timestr, "%H:%M:%S").time()
    for time_obj, display in Reservation.time.field.choices:
        if time_obj == tt:
            return time_obj
    raise forms.ValidationError(f"Invalid time choice: {tt}")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Using the customized ReservationAdminForm above and register
    it in the admin
    """
    form = ReservationAdminForm
    list_display = ('name', 'date', 'time', )
    search_fields = ['name']
    list_filter = ('name', 'date', )
