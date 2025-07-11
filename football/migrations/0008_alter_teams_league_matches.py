# Generated by Django 5.1.7 on 2025-03-17 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('football', '0007_alter_teams_cups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='football.leagues'),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_id', models.PositiveIntegerField()),
                ('match_date', models.CharField(max_length=5)),
                ('match_time', models.TimeField()),
                ('status', models.CharField(choices=[('Запланований', 'Scheduled'), ('Завершений', 'Finished')], default='Запланований', max_length=20)),
                ('home_team_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('away_team_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='football.teams')),
                ('competition_type', models.ForeignKey(limit_choices_to={'model__in': ('leagues', 'cups')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='football.teams')),
            ],
        ),
    ]
