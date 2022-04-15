from django.shortcuts import render
from .models import Team
from django.http import HttpResponse


def index(request):
    return render(request, 'League_App/index.html')


def teams(request):
    """Show all teams"""
    all_teams = Team.objects.order_by('team_name')
    context = {'team': all_teams}
    return render(request, 'League_App/team.html', context)

