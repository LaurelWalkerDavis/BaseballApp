from django import forms
from .models import League, Team, Player


class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['league_name']
        labels = {'league_name': ''}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'wins', 'losses', 'games_played']
        labels = {'team_name': 'Team Name',
                  'wins': 'Number of wins',
                  'losses': 'Number of losses',
                  'games_played': 'Number of games played'}


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['last_name', 'full_name', 'hits', 'singles', 'doubles', 'triples',
                  'at_bats', 'home_runs', 'putouts', 'assists', 'chances']
        labels = {'last_name': 'Last Name',
                  'full_name': 'Full Name',
                  'hits': 'Hits',
                  'singles': 'Singles',
                  'doubles': 'Doubles',
                  'triples': 'Triples',
                  'at_bats': 'At Bats',
                  'home_runs': 'Home Runs',
                  'putouts': 'Putouts',
                  'assists': 'Assists',
                  'chances': 'Chances'}
