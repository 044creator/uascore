# Generated by Django 5.1.7 on 2025-03-16 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_news_alter_countries_image_alter_leagues_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/football/news/'),
        ),
        migrations.AlterField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/football/players/'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/football/teams/'),
        ),
        migrations.CreateModel(
            name='Cups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uk', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/football/cups/')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cups', to='football.countries')),
            ],
            options={
                'verbose_name': 'Кубок',
                'verbose_name_plural': 'Кубки',
            },
        ),
        migrations.AddField(
            model_name='teams',
            name='cup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='football.cups'),
        ),
    ]
