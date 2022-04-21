from django.db import models

# Create your models here.
from django.db.models import SET_DEFAULT


class League(models.Model):
    league_name = models.CharField(max_length=200, default="My League")
    # clashes with "league = models.ForeignKey(League, on_delete=models.CASCADE)" in Team
    # all_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')

    def __str__(self):
        return f"League: <{self.league_name}"


class Team(models.Model):
    # identity fields
    team_name = models.CharField(max_length=200, default="My Team")

    # membership fields
    # t_players = models.ManyToManyField(Player, related_name='players', related_query_name='player')
    # league = models.ManyToOneRel(League, related_name='league', on_delete=models.CASCADE)
    league = models.ForeignKey(League, related_name='league', default=None, on_delete=models.CASCADE)

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
               f"\nWins: {self.wins}\t|\tLosses: {self.losses}, " \
               f"\nGames Played: {self.games_played}>"

    class Meta:
        verbose_name_plural = 'teams'


class Player(models.Model):
    # identity fields
    last_name = models.CharField(max_length=200, default=None)
    full_name = models.CharField(max_length=200, default=None)

    # membership fields
    team = models.ForeignKey(Team, related_name='team', default=None, on_delete=models.CASCADE)

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
    # batting_average = models.DecimalField(max_digits=4, decimal_places=3, default=.000)
    # fielding_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)

    # Display Fields
    DisplayFields = ['id', 'full_name', 'batting_average', 'fielding_percentage']

    @property
    def get_batting_average(self):
        avg = self.get_hits / self.at_bats
        str_avg = format(avg, "0.3f")
        return str_avg

    @property
    def get_hits(self):
        return self.singles + self.doubles + self.triples + self.home_runs

    @property
    def get_fielding_percentage(self):
        avg = (self.putouts + self.assists) / self.chances
        str_avg = format(avg, "0.3f")
        return str_avg

    def __str__(self):
        return f"Player <{self.full_name}:" \
               f"\nBatting Avg: {self.get_batting_average}" \
               f"\nFielding Percentage: {self.get_fielding_percentage}>"

    class Meta:
        verbose_name_plural = 'players'
