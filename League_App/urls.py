from django.urls import path

from . import views

app_name = 'League_App'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # League page.
    path('league/', views.league, name='league'),
    # Team page.
    path('teams/', views.team, name='team'),
    # Single player page
    path('players/', views.player, name='player')
]

