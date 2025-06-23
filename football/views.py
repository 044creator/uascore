from datetime import datetime
from django.shortcuts import render
from .models import Countries, Leagues, News, Matches, Teams
from collections import defaultdict, OrderedDict

def home(request):
    date_str = request.GET.get("date", datetime.today().strftime("%d/%m"))
    try:
        selected_date = datetime.strptime(date_str, "%d/%m")
    except ValueError:
        selected_date = datetime.today()
    selected_date = selected_date.strftime("%d/%m")

    leagues_with_matches = []

    for league in Leagues.objects.all():
        matches = league.matches.filter(match_date=selected_date).order_by('tour', 'match_time', 'match_date', 'status')

        if matches.exists():
            matches_by_tour = defaultdict(list)
            for match in matches:
                matches_by_tour[match.tour].append(match)

            leagues_with_matches.append({
                'league': league,
                'matches_by_tour': dict(matches_by_tour)
            })

    context = {
        'selected_date': selected_date,
        'leagues_with_matches': leagues_with_matches
    }
    return render(request, 'football/index.html', context)

def league_planned_matches(request, country_slug, league_slug):
    league = Leagues.objects.get(slug=league_slug)
    planned_matches = league.matches.filter(status='planned').order_by('tour', 'match_date', 'match_time')

    matches_by_tour = defaultdict(list)
    for match in planned_matches:
        matches_by_tour[match.tour].append(match)
    context = {'league': league,
               'matches_by_tour': dict(matches_by_tour)}
    return render(request, 'football/league_planned.html', context)

def league_finished_matches(request, country_slug, league_slug):
    league = Leagues.objects.get(slug=league_slug)
    finished_matches = league.matches.filter(status='finished').order_by('tour', 'match_date', 'match_time')
    matches_by_tour = defaultdict(list)
    for match in finished_matches:
        matches_by_tour[match.tour].append(match)

    matches_by_tour_sorted = OrderedDict(
        sorted(matches_by_tour.items(), reverse=True)
    )
    context = {'league': league,
               'matches_by_tour': dict(matches_by_tour_sorted)}
    return render(request, 'football/league_finished.html', context)

def league_table(request, country_slug, league_slug):
    league = Leagues.objects.get(slug=league_slug)
    table = league.tables.first()
    table_lines = table.lines.all().order_by('place') if table else []

    context = {
        'title': f'Таблиця – {league.name_uk}',
        'league': league,
        'table_lines': table_lines,
    }
    return render(request, 'football/league_table.html', context)

def country_preview(request, country_slug):
    print(Matches.objects.values_list('status', flat=True).distinct())
    matches_status = request.GET.get('action', 'finished')
    country = Countries.objects.get(slug=country_slug)
    league_with_matches = []
    for league in country.leagues.all():
        matches = league.matches.filter(status=matches_status).order_by('tour', 'match_date', 'match_time')
        if matches.exists():
            grouped = defaultdict(list)
            for match in matches:
                grouped[match.tour].append(match)
            league_with_matches.append({
                'league': league,
                'matches_by_tour': dict(grouped)
            })

    context = {'country': country,
               'league_with_matches': league_with_matches,
               }
    return render(request, 'football/country.html', context)

def team_planned_matches(request, team_slug):
    team = Teams.objects.get(slug=team_slug)
    planned_matches_home = set(team.home_matches.filter(status='planned'))
    planned_matches_away = set(team.away_matches.filter(status='planned'))

    planned_matches = sorted(
        planned_matches_home | planned_matches_away,
        key=lambda m: (m.tour, m.match_date, m.match_time)
    )

    matches_by_league = defaultdict(list)
    for match in planned_matches:
        matches_by_league[match.league].append(match)

    print(matches_by_league)
    print(matches_by_league.keys())

    context = {'team': team,
               'planned_matches': dict(matches_by_league)}
    return render(request, 'football/team_planned.html', context)


def team_finished_matches(request, team_slug):
    team = Teams.objects.get(slug=team_slug)
    finished_matches_home = set(team.home_matches.filter(status='finished'))
    finished_matches_away = set(team.away_matches.filter(status='finished'))

    finished_matches = sorted(
        finished_matches_home | finished_matches_away,
        key=lambda m: (m.tour, m.match_date, m.match_time)
    )

    matches_by_league = defaultdict(list)
    for match in finished_matches:
        matches_by_league[match.league].append(match)

    print(matches_by_league)
    print(matches_by_league.keys())

    context = {'team': team,
               'finished_matches': dict(matches_by_league)}
    return render(request, 'football/team_finished.html', context)