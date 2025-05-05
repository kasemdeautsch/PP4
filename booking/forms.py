from datetime import datetime, time, date, timedelta
from django import forms
from .models import Reservation
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


class ReservationForm(forms.ModelForm):
    """
    Form to render in the template with choices list of times applied on
    the time field (converted to time object).

    """
    time = forms.ChoiceField(choices=values, widget=forms.Select)

    class Meta:
        """
        Meta class using the :model: `Booking.Reservation`.
        """
        model = Reservation
        fields = ('name',  'date', 'time', 'email', 'notes',)

    def clean_time(self):
        """
        Function to convert the time field to time object if neede.
        """
        timestr = self.cleaned_data['time']
        return datetime.strptime(timestr, "%H:%M:%S").time()

    def clean_date(self):
        """
        Function to check if the chosen date is within a period of one month,
        raises error if it is not whtin that period.
        """
        today = date.today()
        after_one_month = today + timedelta(days=30)
        new_date = self.cleaned_data.get('date')
        if new_date >= today and new_date <= after_one_month:
            return new_date
        raise forms.ValidationError(
            f"Please enter a date within one month"
            f"({today} to {after_one_month})")
