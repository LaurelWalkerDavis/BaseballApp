from django.shortcuts import render
from .models import Team, League, Player
from django.http import HttpResponse


def index(request):
    return render(request, 'League_App/index.html')


def league(request):
    """Show all teams"""
    league_name = League.league_name
    all_teams = Team.objects.order_by('team_name')
    # all_players = League.all_players.order_by('last_name')
    # context = {'team': all_teams, 'player': all_players}
    context = {'name': league_name, 'team': all_teams}
    return render(request, 'League_App/league.html', context)


def team(request):
    """Show team stats"""
    team_players = Team.t_players.order_by('last_name')
    context = {'player': team_players}
    return render(request, 'League_App/team.html', context)


def player(request, player_id):
    """Show player profile"""
    player_name = Player.objects.order_by('last_name')
    context = {'name': player_name}
    return render(request, 'League_App/player.html', context)

