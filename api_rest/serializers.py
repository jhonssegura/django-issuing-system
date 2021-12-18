from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from registry.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_cod', 'event_nom', 'event_date_init', 'even_date_end', 'event_site', 'event_url']


class MagazineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magazine
        fields = ['magazine_code', 'magazine_name', 'magazine_date', 'magazine_arb', 'magazine_cenditel', 'magazine_url']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'course_date_init', 'course_date_end']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['project_code', 'project_name', 'project_date_init', 'project_date_end', 'project_poa']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['book_code', 'book_name', 'book_date', 'book_cenditel', 'book_url']


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ['participant_code', 'participant_document', 'participant_name', 'participant_lastname', 'participant_email']


class ResearcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Researcher
        fields = ['researcher_code', 'researcher_document', 'researcher_name', 'researcher_lastname', 'reseracher_active']
