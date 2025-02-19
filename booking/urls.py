from . import views
from django.urls import path

urlpatterns = [
    path('make/', views.make_reservation, name='make_reservation'),
    path('reservations/', views.reservation_list, name='reservations'),
    path('reservations/edit_reservation/<int:reservation_id>',
         views.reservation_edit, name='reservation_edit'),

    path('reservations/delete_reservation/<int:reservation_id>',
         views.reservation_delete, name='reservation_delete'),

    path('', views.Home.as_view(), name='home'),
]
