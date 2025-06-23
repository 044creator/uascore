from django.db import models
from django.urls import reverse_lazy


class Countries(models.Model):
    name_uk = models.CharField(max_length=100)
    rating_uefa = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='img/football/countries/', blank=True,
                              null=True)

    def get_absolute_url(self):
        return reverse_lazy('football:country',
                            kwargs={'country_slug': self.slug})

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.name_uk


class TournamentFormat(models.TextChoices):
    LEAGUE = 'Ліга'
    CUP = 'Кубок'
    MIXED = 'Міксований'


class Leagues(models.Model):
    name_uk = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE,
                                related_name='leagues')
    tournament_format = models.CharField(choices=TournamentFormat.choices,
                                         max_length=100,
                                         default=TournamentFormat.LEAGUE)
    image = models.ImageField(upload_to='img/football/leagues/', blank=True,
                              null=True)

    def get_absolute_url(self):
        return reverse_lazy('football:league_planned', kwargs={'country_slug': self.country.slug, 'league_slug': self.slug})

    class Meta:
        verbose_name = 'Ліга'
        verbose_name_plural = 'Ліги'

    def __str__(self):
        return f'{self.country.name_uk} - {self.name_uk}'


class Teams(models.Model):
    name_uk = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    country = models.ForeignKey(Countries,
                                on_delete=models.CASCADE,
                                default=2,
                                related_name='teams')
    league = models.ManyToManyField(Leagues,
                                    related_name='teams')
    image = models.ImageField(upload_to='img/football/teams/', blank=True,
                              null=True)

    def get_absolute_url(self):
        return reverse_lazy('football:team', kwargs={
            'team_slug': self.slug})


    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команди'

    def __str__(self):
        return self.name_uk


class Positions(models.TextChoices):
    GK = 'Воротар', 'ВРТ'
    LB = 'Лівий захисник', 'ЛЗ'
    CB = 'Центральний захисник', 'ЦЗ'
    RB = 'Правий захисник', 'ПЗ'
    CDM = 'Опорний півзахисник', 'ЦОП'
    CM = 'Центральний півзахисник', 'ЦП'
    CAM = 'Атакувальний півзахисник', 'ЦАС'
    LM = 'Лівий півзахисник', 'ЛП'
    RM = 'Правий півзахисник', 'ПП'
    LW = 'Лівий вінгер', 'ЛВ'
    RW = 'Правий вінгер', 'ПВ'
    ST = 'Нападник', 'НАП'


class Players(models.Model):
    name_uk = models.CharField(max_length=100)
    position = models.CharField(choices=Positions.choices, max_length=100)
    birth_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/football/players/', blank=True,
                              null=True)
    country = models.ForeignKey(Countries,
                                on_delete=models.CASCADE,
                                related_name='players',
                                default=1)
    team = models.ForeignKey(Teams,
                             on_delete=models.CASCADE,
                             related_name='players',
                             default=1)

    class Meta:
        verbose_name = 'Гравець'
        verbose_name_plural = 'Гравці'

    def __str__(self):
        return self.name_uk


class News(models.Model):
    title_uk = models.CharField(max_length=100)
    text_uk = models.TextField()
    image = models.ImageField(upload_to='img/football/news/', blank=True,
                              null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-date']

    def __str__(self):
        return self.title_uk

class MatchStats(models.TextChoices):
    PLANNED = 'planned'
    FINISHED = 'finished'

class Matches(models.Model):
    home_team = models.ForeignKey(Teams, on_delete=models.CASCADE,
                                  related_name='home_matches')
    away_team = models.ForeignKey(Teams, on_delete=models.CASCADE,
                                  related_name='away_matches')
    status = models.CharField(choices=MatchStats.choices, max_length=20,
                              default=MatchStats.PLANNED)
    match_date = models.CharField(max_length=5)
    match_time = models.TimeField()
    home_goals = models.CharField(default='-', max_length=2)
    away_goals = models.CharField(default='-', max_length=2)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE,
                               related_name='matches', default=1)
    tour = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчі'
        ordering = ['match_date', 'match_time']

    def __str__(self):
        return f"{self.home_team.name_uk} vs. {self.away_team.name_uk}, {self.match_date} {self.match_time}"

class Table(models.Model):
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='tables')

    class Meta:
        verbose_name = 'Таблиця'
        verbose_name_plural = 'Таблиці'

    def __str__(self):
        return f"Таблиця - {self.league.name_uk}"

class TableLines(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='lines')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    games = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)

    goals_for = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)
    goal_diff = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    place = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Позиція в таблиці'
        verbose_name_plural = 'Позиції в таблицях'
        ordering = ['id']

    def __str__(self):
        return f"{self.team.name_uk} ({self.table.league.name_uk}) – {self.points} очок"
