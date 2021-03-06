from django.shortcuts import render, redirect
from .models import Team, League, Player
from .forms import LeagueForm, TeamForm, PlayerForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


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
    team_obj = Team.objects.get(id=team_id)
    team_players = Player.objects.filter(team_id=team_id)
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


@login_required
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


@login_required
def new_team(request, league_id):
    """ add a new team """
    league = League.objects.get(id=league_id)
    if request.method != 'POST':
        # no data submitted; create a blank form.
        form = TeamForm()
    else:
        # POST data submitted; process data.
        form = TeamForm(data=request.POST)
        if form.is_valid():
            new_team = form.save(commit=False)
            new_team.owner = request.user
            new_team.league = league
            new_team.save()
            return redirect('League_App:league')
            #return redirect('League_App:league', league_id=league_id)
    # Display a blank or invalid form.
    context = {'league': league, 'form': form}
    return render(request, 'League_App/new_team.html', context)


@login_required
def new_player(request, team_id):
    """ add a new team """
    #new_player = Player.objects.get()
    team = Team.objects.get(id=team_id)
    # make sure only team owner can access this page
    if team.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # no data submitted; create a blank form.
        form = PlayerForm()
    else:
        # POST data submitted; process data.
        form = PlayerForm(data=request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.team = team
            new_player.owner = request.user
            new_player.save()
            return redirect('League_App:league')
            #return redirect('League_App:league', league_id=league_id)
    # Display a blank or invalid form.
    context = {'team': team, 'form': form}
    return render(request, 'League_App/new_player.html', context)


@login_required
def edit_team(request, team_id):
    """ edit an existing league """
    team = Team.objects.get(id=team_id)
    league = team.league
    # make sure only team owner can access this page
    if team.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current team.
        form = TeamForm(instance=team)
    else:
        # POST data submitted; process data.
        form = TeamForm(instance=team, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('League_App:league')
    context = {'team': team, 'league': league, 'form': form}
    return render(request, 'League_App/edit_team.html', context)


@login_required
def edit_player(request, player_id):
    """ edit an existing league """
    player = Player.objects.get(id=player_id)
    team = player.team
    # make sure only team owner can access this page
    if player.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current team.
        form = PlayerForm(instance=player)
    else:
        # POST data submitted; process data.
        form = PlayerForm(instance=player, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('League_App:team', team_id=team.id)
    context = {'player': player, 'team': team, 'form': form}
    return render(request, 'League_App/edit_player.html', context)
