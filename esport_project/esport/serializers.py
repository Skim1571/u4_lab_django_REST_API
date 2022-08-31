from rest_framework import serializers
from .models import Team, Player

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  players = serializers.HyperlinkedRelatedField(
    view_name='player_detail',
    many=True,
    read_only=True
  )

  class Meta:
    model = Team
    fields = ('id','name','nationality','team_logo_url','players')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField(
    view_name='team_detail',
    read_only=True
  )
  class Meta:
    model = Player
    fields = ('id','team','name','handle')