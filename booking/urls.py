from . import views
from django.urls import path

urlpatterns = [
    path('res/', views.ReservationList.as_view(), name='home'),
    #path('', views.index, name='index'),
    # path('reservation_create', views.ResevationCreateView.as_view(), name="create-booking")
]
