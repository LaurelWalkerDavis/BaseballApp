# Generated by Django 4.0.4 on 2022-04-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League_App', '0005_alter_player_assists_alter_player_at_bats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='at_bats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='batting_average',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='player',
            name='chances',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='doubles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='errors',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='fielding_percentage',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='player',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='home_runs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='putouts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='rbi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='triples',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='games_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_at_bats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_batting_average',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_doubles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_home_runs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_runs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='t_triples',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
