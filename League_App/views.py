from django.shortcuts import render, redirect
from .models import Team, League, Player
from .forms import LeagueForm
from django.http import HttpResponse


def index(request):
    return render(request, 'League_App/index.html')


def league(request):
    """Show all teams"""
    league_obj = League.objects.get()
    all_teams_obj = Team.objects.order_by('team_name')
    all_players = Player.objects.order_by('last_name')
    context = {'league': league_obj,
               'all_teams': all_teams_obj,
               'all_players': all_players}
    return render(request, 'League_App/league.html', context)


def team(request, team_id):
    """Show team stats"""
    team_obj = Team.objects.get(team=team_id)
    team_players = Player.objects.filter(team=team_id)
    context = {'team': team_obj,
               'team_players': team_players}
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


def new_league(request):
    """ add a new league"""
    if request.method != 'POST':
        # no data submitted; create a blank form.
        form = LeagueForm()
    else:
        # POST data submitted; process data.
        form = LeagueForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('League_App:league')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'League_App/new_league.html', context)