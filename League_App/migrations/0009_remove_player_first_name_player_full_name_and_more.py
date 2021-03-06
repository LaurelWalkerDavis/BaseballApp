# Generated by Django 4.0.4 on 2022-04-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League_App', '0008_league_remove_player_assists_remove_player_at_bats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='first_name',
        ),
        migrations.AddField(
            model_name='player',
            name='full_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_players',
            field=models.ManyToManyField(to='League_App.player'),
        ),
    ]
