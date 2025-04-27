from django import forms
from .models import Reservation
from datetime import time
import datetime

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
        fields = ('name', 'email', 'date', 'time', 'notes',)
    #print('after Meta-class--')
    #print()
    
    def clean_time(self):
        """
        Function to convert the time field to time object if neede.
        """
        timestr = self.cleaned_data['time']
        #timestr = "7:20:3"
        #print('3-self.cleaned_data:', self.cleaned_data)
        #print("4-time field:-----", timestr)
        #print("5-type(timestr): ", type(timestr))
        tt=datetime.datetime.strptime(timestr, "%H:%M:%S").time()
        #print("6-tt type: ", type(tt))
        #print("7-date type: ", type(self.cleaned_data['date']))
        #print("8-time after:", datetime.datetime.strptime(timestr, "%H:%M:%S").time())
        #print("9-self.time: ", self.cleaned_data['time'], "type: ", type(self.cleaned_data['time']))
        return datetime.datetime.strptime(timestr, "%H:%M:%S").time()

    