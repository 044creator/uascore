from django.apps import AppConfig


class FootballConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'football'

    def ready(self):
        import football.signals

