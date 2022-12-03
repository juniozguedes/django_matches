from django.shortcuts import render
from match.models import Match
from rest_framework import viewsets
from .serializers import MatchSerializer

# ViewSets define the view behavior.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer