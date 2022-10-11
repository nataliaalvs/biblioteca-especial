from django.apps import AppConfig


class BibConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bib'
    def ready(self):
        import bib.signals
    