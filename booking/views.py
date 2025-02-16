from django.views.generic import ListView, CreateView,TemplateView
from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation

# Create your views here.


class Home(TemplateView):
    """
    View to render the home page
    """

    template_name = "booking/index.html"


def reservation_list(request):

    #user = get_object_or_404(User, user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
            
    return render(
        request,
        "booking/reservation_list.html",
        {
            "reservations": reservations,
        },
        
    )


def make_reservation(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Yor have successfully booked a reservation!"
            )
    reservation_form = ReservationForm()

    return render(
        request,
        "booking/make_reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


# class ReservationListView(ListView):

"""""
class ReservationList(ListView):
    # model = Reservation
    context_object_name = 'reservations'
    # queryset = Reservation.objects.all()
    # queryset = Reservation.objects.filter(name='jamal')
    queryset = Reservation.objects.all().order_by("-date")
    template_name = "booking/index.html"
    #paginate_by = 6
    

"""
"""
class ResevationCreateView(CreateView):
    model = Reservation
    fields = ["name", "date", "time", "time", "notes", "user"]
"""
