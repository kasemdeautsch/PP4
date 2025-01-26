from django.views.generic import ListView
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Reservation

# Create your views here.

"""
def test(request):
    return HttpResponse("Hello, Reservations")
"""

# class ReservationListView(ListView):


class ReservationList(ListView):
    # model = Reservation
    context_object_name = 'reservations'
    # queryset = Reservation.objects.all()
    # queryset = Reservation.objects.filter(name='jamal')
    queryset = Reservation.objects.all().order_by("-date")
    # template_name = "reservation_list.html"
