from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api_rest.serializers import EventSerializer, UserSerializer, GroupSerializer
from registry.models import Event

class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allow users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows events to be viewed or edited
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer