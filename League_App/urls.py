from django.urls import path

from . import views

app_name = 'League_App'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Teams page.
    path('team/', views.teams, name='team')
]