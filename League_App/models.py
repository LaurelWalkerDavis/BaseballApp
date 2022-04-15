from django.db import models


# Create your models here.
from django.db.models import SET_DEFAULT


class Player(models.Model):
    team = models.ForeignKey('Team', related_name='players', related_query_name='player',
                             default=None, on_delete=SET_DEFAULT)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    putouts = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    errors = models.IntegerField(default=0)
    chances = models.IntegerField(default=0)
    fielding_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)

    def __str__(self):
        return f"Player <{self.first_name} {self.last_name}, \nHits: {self.hits}, \nAt Bats: {self.at_bats}, " \
               f"\nRBIs: {self.rbi}, \nHome Runs: {self.home_runs} \nBatting Avg: {self.batting_average}" \
               f"\n Putouts: {self.putouts}, \nAssists: {self.assists}, \nErrors: {self.errors}," \
               f"\n Chances: {self.chances}, \nFielding Percentage: {self.fielding_percentage}>"

    class Meta:
        indexes = [models.Index(fields=['last_name'])]
        ordering = ['-last_name']


class League(models.Model):
    league_name = models.CharField(max_length=200, default="My League")
    # clashes with "league = models.ForeignKey(League, on_delete=models.CASCADE)" in Team
    #  all_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')

    def __str__(self):
        return f"League: <{self.league_name}>"

    class Meta:
        indexes = [models.Index(fields=['league_name'])]
        ordering = ['-league_name']


class Team(models.Model):
    team_name = models.CharField(max_length=200, default=None)
    t_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')
    t_hits = models.IntegerField(default=0)
    t_doubles = models.IntegerField(default=0)
    t_triples = models.IntegerField(default=0)
    t_home_runs = models.IntegerField(default=0)
    t_at_bats = models.IntegerField(default=0)
    t_runs = models.IntegerField(default=0)
    t_batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    league = models.ForeignKey(League, on_delete=models.CASCADE, default=League.league_name)

    def __str__(self):
        return f"Team <{self.team_name}, \nHits: {self.t_hits}, \nDoubles: {self.t_doubles}, " \
               f"\nTriples: {self.t_triples} \nHome Runs: {self.t_home_runs}, \nAt Bats: {self.t_at_bats}," \
               f"\nBatting Avg: {self.t_batting_average}, \nWins: {self.wins}, \nLosses: {self.losses}, " \
               f"\nGames Played: {self.games_played}>"

    class Meta:
        indexes = [models.Index(fields=['team_name'])]
        ordering = ['-team_name']

