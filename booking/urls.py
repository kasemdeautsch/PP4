from . import views
from django.urls import path

urlpatterns = [
    path('reservations/edit_reservation/<int:reservation_id>', views.edit_reservation, name='edit_reservation'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('reservations/', views.reservation_list, name='reservations'),
    path('', views.Home.as_view(), name='home'),
    # path('reservation_create', views.ResevationCreateView.as_view(), name="create-booking")
]
