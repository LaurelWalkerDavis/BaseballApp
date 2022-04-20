from django.db import models

# Create your models here.
from django.db.models import SET_DEFAULT


class League(models.Model):
    league_name = models.CharField(max_length=200, default="My League")
    # clashes with "league = models.ForeignKey(League, on_delete=models.CASCADE)" in Team
    #  all_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')

    def __str__(self):
        return f"League: <{self.league_name}>"

    # class Meta:
    #     indexes = [models.Index(fields=['league_name'])]
    #     ordering = ['-league_name']

class Team(models.Model):
    # identity fields
    team_name = models.CharField(max_length=200, default=None)

    # membership fields
    # t_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    # data fields
    # t_hits = models.IntegerField(default=0)
    # t_doubles = models.IntegerField(default=0)
    # t_triples = models.IntegerField(default=0)
    # t_home_runs = models.IntegerField(default=0)
    # t_at_bats = models.IntegerField(default=0)
    # t_runs = models.IntegerField(default=0)
    # t_batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return f"Team <{self.team_name}" \
               f"\nWins: {self.wins}, \nLosses: {self.losses}, " \
               f"\nGames Played: {self.games_played}>" \
               f"\nTeam Members: {self.t_players}>"

    # class Meta:
    #     indexes = [models.Index(fields=['team_name'])]
    #     ordering = ['-team_name']

class Player(models.Model):
    # identity fields
    last_name = models.CharField(max_length=200, default=None)
    full_name = models.CharField(max_length=200, default=None)

    # membership fields
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # league = models.ForeignKey('League', related_name=

    # data fields
    hits = models.IntegerField(default=0)
    singles = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    putouts = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    chances = models.IntegerField(default=0)
    batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    fielding_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)

    def get_batting_average(self):
        return self.get_hits() / self.at_bats

    def get_hits(self):
        return self.singles + self.doubles + self.triples + self.home_runs

    def get_fielding_percentage(self):
        return (self.putouts + self.assists) / self.chances

    # batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    # putouts = models.IntegerField(default=0)
    # assists = models.IntegerField(default=0)
    # errors = models.IntegerField(default=0)
    # chances = models.IntegerField(default=0)
    # fielding_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)

    def __str__(self):
        return f"Player <{self.full_name}" \
               f"\nBatting Avg: {self.batting_average}" \
               f"\nFielding Percentage: {self.fielding_percentage}>"

    # class Meta:
    #     indexes = [models.Index(fields=['last_name'])]
    #     ordering = ['-last_name']

