# Serializers define the API representation.
from rest_framework import serializers
from match.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['local', 'away', 'stadium', 'local_goals', 'away_goals']
