from django.views.generic import ListView, CreateView,TemplateView
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Reservation

# Create your views here.


class Home(TemplateView):
    """
    View to render the home page
    """

    template_name = "booking/index.html"


"""
def test(request):
    return HttpResponse("Hello, Reservations")
"""

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

"""""
def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method+' Ok')
"""