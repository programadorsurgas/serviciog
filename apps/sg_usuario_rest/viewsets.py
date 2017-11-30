from rest_framework import generics
from rest_framework import viewsets

from apps.sg_usuario.models import Usr_system
from .serializers import Usr_systemSerializer


class Usr_systemViewSet(viewsets.ModelViewSet):
    queryset = Usr_system.objects.all()
    serializer_class = Usr_systemSerializer
