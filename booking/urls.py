from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationList.as_view(), name='home'),
    # path('reservation_create', views.ResevationCreateView.as_view(), name="create-booking")
]
