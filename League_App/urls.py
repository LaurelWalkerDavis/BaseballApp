from django.urls import path

from . import views

app_name = 'League_App'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Team page.
    path('team/', views.team, name='team'),
    # League page.
    path('league/', views.league, name='league'),
    # Single player page
    path('player/<int:player_id>/', views.player, name='player')
]

