from rest_framework import serializers

from apps.sg_usuario.models import Usr_system


class Usr_systemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usr_system
        fields = ('name', 'dni')
