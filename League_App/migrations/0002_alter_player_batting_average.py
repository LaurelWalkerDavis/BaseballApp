# Generated by Django 4.0.4 on 2022-04-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='batting_average',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
