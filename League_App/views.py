from django.shortcuts import render
from .models import Team, League, Player
from django.http import HttpResponse


def index(request):
    return render(request, 'League_App/index.html')


def league(request):
    """Show all teams"""
    league_name = League.league_name
    all_teams = Team.objects.order_by('team_name')
    context = {'name': league_name, 'team': all_teams}
    return render(request, 'League_App/league.html', context)


def team(request):
    """Show team stats"""
    team_players = Team.t_players
    context = {'player': team_players}
    return render(request, 'League_App/team.html', context)


def player(request, player_id):
    """Show player profile"""
    player_obj = Player.objects.get(id=player_id)
    context = {'player': player_obj}
    return render(request, 'League_App/player.html', context)

