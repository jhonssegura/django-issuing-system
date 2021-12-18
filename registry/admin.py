from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_cod', 'event_nom', 'event_date_init', 'even_date_end', 'event_site', 'event_url']

admin.site.register(Event, EventAdmin)