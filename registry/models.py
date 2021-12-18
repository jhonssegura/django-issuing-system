from django.db import models

class Event(models.Model):
    event_cod = models.CharField('Codigo Identificacion', max_length=200, unique=True)
    event_nom = models.CharField('Nombre del Evento', max_length=200)
    event_date_init = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    even_date_end = models.DateField('Fecha de Finalizacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    event_site = models.TextField('Lugar del Evento', max_length=500, null=True, blank=True)
    event_url = models.URLField('Pagina Web', null=True, blank=True)

    def __str__(self):
        return self.event_cod