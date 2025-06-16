from datetime import datetime
from django.shortcuts import render
from .models import Countries, Leagues, News, Matches, Teams


def home(request):
    countries = Countries.objects.all().order_by('rating_uefa')
    news = News.objects.all()[:3]

    date_str = request.GET.get("date", datetime.today().strftime("%d/%m"))
    try:
        selected_date = datetime.strptime(date_str, "%d/%m")
    except ValueError:
        selected_date = datetime.today()
    selected_date = selected_date.strftime("%d/%m")

    leagues = Leagues.objects.all()
    leagues_with_matches = []
    for league in leagues:
        matches_today = league.matches.filter(match_date=selected_date)
        if matches_today.exists():
            leagues_with_matches.append(
                {'league': league, 'matches': matches_today})

    context = {'countries': countries,
               'news': news,
               'selected_date': selected_date,
               'leagues_with_matches': leagues_with_matches
               }
    return render(request, 'football/index.html', context)

def league_preview(request, country_slug, league_slug):
    countries = Countries.objects.all().order_by('rating_uefa')
    news = News.objects.all()[:3]

    league = Leagues.objects.get(slug=league_slug)
    teams = league.teams.all()
    context = {'league': league,
               'teams': teams,
               'countries': countries,
               'news': news}
    return render(request, 'football/league.html', context)



def country_preview(request, country_slug):
    countries = Countries.objects.all().order_by('rating_uefa')
    news = News.objects.all()[:3]

    matches_status = request.GET.get('action', 'Завершений')
    country = Countries.objects.get(slug=country_slug)
    league_with_matches = []
    for league in country.leagues.all():
        matches = league.matches.filter(status=matches_status).order_by('-match_date', '-match_time')
        if matches.exists():
            league_with_matches.append(
                {'league': league, 'matches': matches})
    context = {'country': country,
               'league_with_matches': league_with_matches,
               'countries': countries,
               'news': news}
    return render(request, 'football/country.html', context)

def team_preview(request, team_slug):
    countries = Countries.objects.all().order_by('rating_uefa')
    news = News.objects.all()[:3]

    team = Teams.objects.get(slug=team_slug)
    context = {'team': team,
               'countries': countries,
               'news': news}
    return render(request, 'football/team.html', context)