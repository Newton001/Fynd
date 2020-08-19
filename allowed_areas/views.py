from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Allowed_areasSerializer
from .models import Allowed_areas


class Allowed_areasViewSet(viewsets.ModelViewSet):
    queryset = Allowed_areas.objects.all().order_by('name')
    serializer_class = Allowed_areasSerializer
# Create your views here.
