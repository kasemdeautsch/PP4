from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def reservations(request):
    return HttpResponse("Hello, Reservations")
