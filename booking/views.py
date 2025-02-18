from django.views.generic import ListView, CreateView,TemplateView
from django.shortcuts import render, get_object_or_404, redirect,reverse
#from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReservationForm
from .models import Reservation
import datetime

# Create your views here.


class Home(TemplateView):
    """
    View to render the home page
    """
    print('datetime.date.today-->>', datetime.date.today())
    print('timezone.now-->>', timezone.now())
    print('datetime.datetime.now()-->>',  datetime.datetime.now())

    template_name = "booking/index.html"


def reservation_list(request):

    user = get_object_or_404(User, username=request.user)
    reservations = Reservation.objects.filter(user=user).order_by('-date')
    reservations_count = reservations.count()
    #reservations = reservations.objects.filter(date >= timezone.now)
    
    return render(
        request,
        "booking/reservation_list.html",
        {
            "reservations": reservations,
            "reservations_count": reservations_count,
        },
        
    )


def make_reservation(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, "Yor have successfully booked!")
        else:
            messages.add_message(request, messages.ERROR, "Error in Booking!, please enter valid fields")
            reservation_form = ReservationForm()
            #return HttpResponseRedirect(reverse("reservations"))
    reservation_form = ReservationForm()

    return render(
        request,
        "booking/make_reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


def edit_reservation(request, reservation_id):
    print(reservation_id)

    if request.method == "POST":
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=reservation)
        if reservation_form.is_valid() and reservation.user == request.user:
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, "Reservation Updated Successfully!")
            reservation_form = ReservationForm()
            return HttpResponseRedirect(reverse("reservations"))
            
        else:
            messages.add_message(request, messages.ERROR, "Error Updating Reservation!")
            reservation_form = ReservationForm()
            return HttpResponseRedirect(reverse("reservations"))

    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation_form = ReservationForm(instance=reservation)

    return render(
        request,
        "booking/edit_reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


def delete_reservation(request, reservation_id):

    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if reservation.user == request.user:
        reservation.delete()
        messages.add_message(request, messages.SUCCESS, "Booking deleted Successfully")
    else:
        messages.add_message(request, messages.SUCCESS, "Error! You can only delete your own Booking.")
    return HttpResponseRedirect(reverse("reservations"))


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
