from django.apps import AppConfig
from .scheduler import updater


class DtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt'

    def ready(self):
        print("Обновление данных через 30 дней...")
        updater.scheduler_start()
