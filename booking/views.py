
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReservationForm
from .models import Reservation
# Create your views here.


class Home(TemplateView):
    """
    Class-based View to render the home page
    """
    template_name = "booking/index.html"


def reservation_list(request):
    """
    Renders the list of reservations(bokkings) for particular user
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
        print("form-before: ")
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(
                request, messages.SUCCESS, "Yor have successfully booked!"
                )
            return HttpResponseRedirect(reverse("reservations"))
        else:
            messages.add_message(
                request, messages.ERROR, "Error in Booking!, "
                                         "please enter valid fields"
                )
    else:
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
    Receives `reservation_id` and fetches the related one from databese.
    Display an individual reservation for edit :model:`booking.Reservation`.
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
        reservation_form = ReservationForm(data=request.POST,
                                           instance=reservation)
        if reservation_form.is_valid() and reservation.user == request.user:
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(
                request, messages.SUCCESS, "Booking Updated Successfully!"
                )
            reservation_form = ReservationForm()
            return HttpResponseRedirect(reverse("reservations"))
        else:
            messages.add_message(
                request, messages.ERROR, "Error Updating Booking!"
                )
    else:
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
    receives `reservation_id` and fetches the related one from databese.
    then deletes it.
    Display an individual reservation for edit :model:`booking.Reservation`.
    **Context**
    ``reservation``
         A single reservation related to the requested user.
    ``reservation_form``
        an instance of :form:`booking.ReservationForm`
    **Template:**

    :template:`booking/edit_reservation.html`
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if reservation.user == request.user:
        reservation.delete()
        messages.add_message(
            request, messages.SUCCESS, "Booking deleted Successfully!"
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            "Error! You can only delete your own Booking."
        )
    return HttpResponseRedirect(reverse("reservations"))
