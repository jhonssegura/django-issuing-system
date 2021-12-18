from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_cod', 'event_nom', 'event_date_init', 'even_date_end', 'event_site', 'event_url']

class MagazineAdmin(admin.ModelAdmin):
    model = Magazine
    list_display = ['magazine_code', 'magazine_name', 'magazine_date', 'magazine_arb', 'magazine_cenditel', 'magazine_url']

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['course_code', 'course_name', 'course_date_init', 'course_date_end']

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['project_code', 'project_name', 'project_date_init', 'project_date_end', 'project_poa']

class BookAdmin(admin.ModelAdmin):
    models = Book
    list_display = ['book_code', 'book_name', 'book_date', 'book_cenditel', 'book_url']

class ParticipantAdmin(admin.ModelAdmin):
    models = Participant
    list_display = ['participant_code', 'participant_document', 'participant_name', 'participant_lastname', 'participant_email']

class ResearcherAdmin(admin.ModelAdmin):
    models = Researcher
    list_display = ['researcher_code', 'researcher_document', 'researcher_name', 'researcher_lastname', 'reseracher_active']

admin.site.register(Event, EventAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Researcher, ResearcherAdmin)