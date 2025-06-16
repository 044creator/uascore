from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "football"

urlpatterns = ([path("", views.home, name="home"),
                path("<str:country_slug>/<str:league_slug>", views.league_preview, name="league"),
                path("<str:country_slug>/", views.country_preview, name="country"),
                path("team/<str:team_slug>/preview/", views.team_preview, name="team"),
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
