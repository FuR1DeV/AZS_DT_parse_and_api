from django.apps import AppConfig


class DtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt'

    def ready(self):
        from .scheduler import updater
        print("Обновление данных через 30 дней...")
        updater.scheduler_start()
