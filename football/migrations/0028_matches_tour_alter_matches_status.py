# Generated by Django 5.1.7 on 2025-06-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0027_alter_matches_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='tour',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='matches',
            name='status',
            field=models.CharField(choices=[('planned', 'Planned'), ('finished', 'Finished')], default='planned', max_length=20),
        ),
    ]
