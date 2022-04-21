from django.urls import path, re_path

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
    path('new_league/', views.new_league, name='new_league')
]
