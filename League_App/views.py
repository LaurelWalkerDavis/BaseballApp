from django.shortcuts import render
from .models import Team, League, Player
from django.http import HttpResponse


def index(request):
    return render(request, 'League_App/index.html')


def league(request):
    """Show all teams"""
    league_name = League.league_name
    all_teams_obj = Team.objects.order_by('team_name')
    all_players = Player.objects.order_by('last_name')
    context = {'league_name': league_name,
               'all_teams': all_teams_obj,
               'all_players': all_players}
    return render(request, 'League_App/league.html', context)


def team(request):
    """Show team stats"""
    team_players = Player.objects.player.all()
    context = {'players': team_players}
    return render(request, 'League_App/team.html', context)


def player(request, player_id):
    """Show player profile"""
    player_obj = Player.objects.get(id=player_id)
    player_batting_average = player_obj.get_batting_average
    player_fielding_percent = player_obj.get_fielding_percentage
    context = {'player': player_obj,
               'batting average': player_batting_average,
               'fielding percentage': player_fielding_percent}
    return render(request, 'League_App/player.html', context)

