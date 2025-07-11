# Generated by Django 5.1.7 on 2025-06-19 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0028_matches_tour_alter_matches_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='football.leagues')),
            ],
            options={
                'verbose_name': 'Таблиця',
                'verbose_name_plural': 'Таблиці',
            },
        ),
        migrations.CreateModel(
            name='TableLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.PositiveIntegerField(default=0)),
                ('wins', models.PositiveIntegerField(default=0)),
                ('draws', models.PositiveIntegerField(default=0)),
                ('losses', models.PositiveIntegerField(default=0)),
                ('goals_for', models.PositiveIntegerField(default=0)),
                ('goals_against', models.PositiveIntegerField(default=0)),
                ('goal_diff', models.IntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('place', models.PositiveIntegerField(default=0)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='football.table')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.teams')),
            ],
            options={
                'verbose_name': 'Позиція в таблиці',
                'verbose_name_plural': 'Позиції в таблицях',
                'ordering': ['id'],
            },
        ),
    ]
