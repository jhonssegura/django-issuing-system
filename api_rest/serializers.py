from django.contrib.auth.models import User, Group
from rest_framework import serializers
from registry.models import Event

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
