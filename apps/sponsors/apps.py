from django.apps import AppConfig


class SponsorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sponsors'

    def ready(self):
        import apps.sponsors.signals