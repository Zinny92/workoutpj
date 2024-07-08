from django.shortcuts import render

# Create your views here.

from .models import Agenda

from rest_framework import permissions, viewsets

from .serializers import AgendaSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]