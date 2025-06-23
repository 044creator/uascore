from django.contrib import admin

from .models import Teams, Players, Countries, Leagues, News, Matches, Table, TableLines


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uk', 'rating_uefa')
    list_display_links = ('name_uk',)
    prepopulated_fields = {'slug': ('name_uk',)}


@admin.register(Leagues)
class LeaguesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uk', 'country')
    list_display_links = ('name_uk',)

    prepopulated_fields = {'slug': ('name_uk',)}


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uk', 'country')
    list_display_links = ('name_uk',)
    search_fields = ('name_uk',)


    prepopulated_fields = {'slug': ('name_uk',)}
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "league":
            country_id = request.POST.get('country')
            if country_id:
                kwargs['queryset'] = Leagues.objects.filter(country_id=country_id) | Leagues.objects.filter(country_id=7)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'home_team', 'away_team', 'league', 'match_date', 'match_time')
    list_editable = ('match_date', 'match_time')

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uk', 'country', 'position', 'team')
    list_display_links = ('name_uk',)

admin.site.register(News)

@admin.action(description="Заповнити таблицю командами з ліги")
def initialize_table_lines(modeladmin, request, queryset):
    for table in queryset:
        table.lines.all().delete()
        place = 1
        for team in table.league.teams.order_by('name_uk'):
            TableLines.objects.create(
                table=table,
                team=team,
                games=0,
                wins=0,
                draws=0,
                losses=0,
                goals_for=0,
                goals_against=0,
                goal_diff=0,
                points=0,
                place=place,
            )
            place += 1

# Адмін для Table
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['league']
    actions = [initialize_table_lines]   # ← додай сюди

@admin.register(TableLines)
class TableLinesAdmin(admin.ModelAdmin):
    pass