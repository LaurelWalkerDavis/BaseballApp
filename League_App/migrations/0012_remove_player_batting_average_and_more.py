# Generated by Django 4.0.4 on 2022-04-20 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('League_App', '0011_alter_league_options_alter_player_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='batting_average',
        ),
        migrations.RemoveField(
            model_name='player',
            name='fielding_percentage',
        ),
    ]
