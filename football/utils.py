from collections import defaultdict
from .models import Table, TableLines

def rebuild_table_from_matches(league):

    table, _ = Table.objects.get_or_create(league=league)
    table.lines.all().delete()

    stats = {
        team: {
            'team': team,
            'games': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'goals_for': 0,
            'goals_against': 0,
            'goal_diff': 0,
            'points': 0,
        }
        for team in league.teams.all()
    }

    matches = league.matches.filter(status='finished')

    for match in matches:
        h = match.home_team
        a = match.away_team

        stats[h]['team'] = h
        stats[a]['team'] = a

        stats[h]['games'] += 1
        stats[a]['games'] += 1

        if match.home_goals != '-' and match.away_goals != '-':
            stats[h]['goals_for'] += int(match.home_goals)
            stats[h]['goals_against'] += int(match.away_goals)
            stats[a]['goals_for'] += int(match.away_goals)
            stats[a]['goals_against'] += int(match.home_goals)

            if match.home_goals > match.away_goals:
                stats[h]['wins'] += 1
                stats[h]['points'] += 3
                stats[a]['losses'] += 1
            elif match.home_goals < match.away_goals:
                stats[a]['wins'] += 1
                stats[a]['points'] += 3
                stats[h]['losses'] += 1
            else:
                stats[h]['draws'] += 1
                stats[a]['draws'] += 1
                stats[h]['points'] += 1
                stats[a]['points'] += 1

    table_lines = list(stats.values())
    for d in table_lines:
        d['goal_diff'] = d['goals_for'] - d['goals_against']

    table_lines.sort(key=lambda x: (-x['points'], -x['goal_diff'], -x['goals_for']))

    for index, data in enumerate(table_lines, start=1):
        TableLines.objects.create(
            table=table,
            team=data['team'],
            games=data['games'],
            wins=data['wins'],
            draws=data['draws'],
            losses=data['losses'],
            goals_for=data['goals_for'],
            goals_against=data['goals_against'],
            goal_diff=data['goals_for'] - data['goals_against'],
            points=data['points'],
            place=index
        )