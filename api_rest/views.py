from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api_rest.serializers import *
from registry.models import *

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


class MagazineViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows magazines to be viewed or edited
    """
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows courses to be viewed or edited
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows books to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows participants to be viewed or edited
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ResearcherViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows researchers to be viewed or edited
    """
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer