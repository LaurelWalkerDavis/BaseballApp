from django import forms
from .models import League, Team


class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['league_name']
        labels = {'league_name': ''}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'league', 'wins', 'losses', 'games_played']
        labels = {'team_name': 'Team Name',
                  'league': 'League Name',
                  'wins': 'Number of wins',
                  'losses': 'Number of losses',
                  'games_played': 'Number of games played'}

