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


class Magazine(models.Model):
    magazine_code = models.CharField('Cidigo de la Revista', max_length=200, unique=True)
    magazine_name = models.CharField('Nombre de la Revista', max_length=200)
    magazine_date = models.DateField('Fecha de Publicacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    magazine_arb = models.BooleanField('Registra Arbitrada?')
    magazine_cenditel = models.BooleanField('Realizada en CENDITEL?')
    magazine_url = models.URLField('Pagina Web', null=True, blank=True)

    def __str__(self):
        return self.magazine_code


class Course(models.Model):
    course_code = models.CharField('Codigo del Curso', max_length=200, unique=True)
    course_name = models.CharField('Nombre del Curso', max_length=200)
    course_date_init = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    course_date_end = models.DateField('Fecha de Finalizacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    # course_enrolled

    def __str__(self):
        return self.course_code


class Project(models.Model):
    project_code = models.CharField('Codigo del Proyecto', max_length=200, unique=True)
    project_name = models.CharField('Nombre del Proyecto', max_length=200)
    project_date_init = models.DateField('Fecha de Inicio', auto_now=False, auto_now_add=False, null=True, blank=True)
    project_date_end = models.DateField('Fecha de Finalizacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    project_poa = models.BooleanField('Pertenece al POA?')

    def __str__(self):
        return self.project_code
    

class Book(models.Model):
    book_code = models.CharField('Codigo del Libro', max_length=200, unique=True)
    book_name = models.CharField('Nombre del Libro', max_length=200)
    book_date = models.DateField('Fecha de Publicación', auto_now=False, auto_now_add=False, null=True, blank=True)
    book_cenditel = models.BooleanField('Realizado en CENDITEL?')
    book_url = models.URLField('Pagina Web', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.book_code


class Participant(models.Model):
    participant_code = models.CharField('Codigo del Participante', max_length=10, unique=True)
    participant_document = models.CharField('Cedula de Identidad', max_length=200, unique=True)
    participant_name = models.CharField('Nombre', max_length=200)
    participant_lastname = models.CharField('Apellido', max_length=200)
    participant_email = models.EmailField('Correo Electronico')

    def __str__(self):
        return self.participant_code


class Researcher(models.Model):
    researcher_code = models.CharField('Codigo del Participante', max_length=10, unique=True)
    researcher_document = models.CharField('Cedula de Identidad', max_length=200, unique=True)
    researcher_name = models.CharField('Nombre', max_length=200)
    researcher_lastname = models.CharField('Apellido', max_length=200)
    #researcher_projects
    reseracher_active = models.BooleanField('Se encuentra activo?')

    def __str__(self):
        return self.researcher_code
