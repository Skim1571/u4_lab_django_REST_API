# Generated by Django 4.1 on 2022-08-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esport', '0002_team_team_logo_url_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='handle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
