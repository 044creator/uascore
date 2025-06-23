from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "football"

urlpatterns = ([path("", views.home, name="home"),
                path("team/<str:team_slug>/planned/", views.team_planned_matches, name="team_planned"),
                path("team/<str:team_slug>/finished/", views.team_finished_matches, name="team_finished"),
                path("<str:country_slug>/<str:league_slug>/planned/", views.league_planned_matches, name="league_planned"),
                path("<str:country_slug>/<str:league_slug>/finished/", views.league_finished_matches, name="league_finished"),
                path("<str:country_slug>/<str:league_slug>/table/", views.league_table, name="league_table"),
                path("<str:country_slug>/", views.country_preview, name="country"),


                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
