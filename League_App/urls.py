from django.urls import path

from . import views

app_name = 'League_App'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # League page.
    path('league/', views.league, name='league'),
    # Team page.
    path('team/<int:team_id>', views.team, name='team'),
    # Single player page
    path('player/<int:player_id>', views.player, name='player'),

    # Adding new league
    path('new_league/', views.new_league, name='new_league'),
    # Adding new team
    path('new_team/<int:league_id>', views.new_team, name='new_team'),
    # Adding new player
    path('new_player/<int:team_id>', views.new_player, name='new_player'),

    # Editing a league
    #path('edit_league/', views.edit_league, name='edit_league'),
    # Editing a team
    path('edit_team/<int:team_id>', views.edit_team, name='edit_team'),
    # Editing a player
    path('edit_player/<int:player_id>', views.edit_player, name='edit_player')
]

