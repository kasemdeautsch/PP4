from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time')
    search_fields = ['name']
    list_filter = ('name', 'date',)
    summernote_fields = ('notes',)


# Register your models here.
#admin.site.register(Reservation)
