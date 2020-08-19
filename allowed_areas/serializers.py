from rest_framework import serializers

from .models import Allowed_areas

class Allowed_areasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allowed_areas
        fields = ('id', 'name', 'location')