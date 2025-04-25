from django.views.generic import ListView, CreateView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect, reverse
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
    
    print('timezone.now-------->>', timezone.now())
    print('timezone.now.today-->>', timezone.now().today())
    print('timezone.now.date-->>', timezone.now().date())
    print('timezone.now.time-->>', timezone.now().time())
    
    print('datetime.date.today-->>', datetime.date.today())
    print('datetime.datetime.now()-->>',  datetime.datetime.now())
    print('timezone.current-->>', timezone.get_current_timezone())
    print('timezone.datetime-->>', timezone.datetime(1,2,3))
    print('timezone.datetime-->>', datetime.date(2012,11,1))
    
    template_name = "booking/index.html"


def reservation_list(request):
    """
    Display a list of reservations :model:`booking.Reservation`.

    **Context**

    ``reservations``
        All reservations of the requested user :model:`booking.Reservation`.
    ``reservations_count``
        A count of reservations related to the user.
    **Template:**

    :template:`booking/reservation_list.html`
    """
    user = get_object_or_404(User, username=request.user)
    #print('User:', user)
    reservations = Reservation.objects.filter(user=user).order_by('-date')
    reservations_count = reservations.count()
    return render(
        request,
        "booking/reservation_list.html",
        {
            "reservations": reservations,
            "reservations_count": reservations_count,
        },
    )


def make_reservation(request):
    """
    Display a form to fill in the required fields :model:`booking.Reservation`.

    **Context**

    ``reservation_form``
        an instance of :form: booking.ReservationForm
    **Template:**

    :template:`booking/make_reservation.html`
    """
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, "Yor have successfully booked!")
            return HttpResponseRedirect(reverse("reservations"))
        else:
            messages.add_message(request, messages.ERROR, "Error in Booking!, please enter valid fields")
            #reservation_form = ReservationForm()
    reservation_form = ReservationForm()

    return render(
        request,
        "booking/make_reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


def reservation_edit(request, reservation_id):
    """
    Display an individual reservation for edit.
    Receives `reservation_id` and fetches the related one from databese.

    **Context**

    ``reservation``
         A single reservation related to the requested user.
    ``reservation_form``
        an instance of :form: booking.ReservationForm
    **Template:**

    :template:`booking/edit_reservation.html`
    """
    if request.method == "POST":
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=reservation)
        if reservation_form.is_valid() and reservation.user == request.user:
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(request, messages.SUCCESS, "Booking Updated Successfully!")
            reservation_form = ReservationForm()
            return HttpResponseRedirect(reverse("reservations"))
            
        else:
            messages.add_message(request, messages.ERROR, "Error Updating Booking!")
            reservation_form = ReservationForm()
            return HttpResponseRedirect(reverse("reservations"))
            #return redirect(reverse('reservations'))

    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation_form = ReservationForm(instance=reservation)

    return render(
        request,
        "booking/edit_reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


def reservation_delete(request, reservation_id):
    """
    Display an individual reservation for edit.
    Receives `reservation_id` and fetches the related one from databese.

    **Context**

    ``reservation``
         A single reservation related to the requested user.
    ``reservation_form``
        an instance of :form: booking.ReservationForm
    **Template:**

    :template:`booking/edit_reservation.html`
    """
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
