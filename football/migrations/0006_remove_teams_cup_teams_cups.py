# Generated by Django 5.1.7 on 2025-03-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_remove_countries_name_remove_cups_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='cup',
        ),
        migrations.AddField(
            model_name='teams',
            name='cups',
            field=models.ManyToManyField(blank=True, to='football.cups'),
        ),
    ]
