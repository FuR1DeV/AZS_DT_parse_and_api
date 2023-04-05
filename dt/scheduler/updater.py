from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from ..views import ParserViewSet


def scheduler_start():
    """Функция создаёт планировщик событий,
    который вызывает функцию main_parser раз в 30 дней (43200 минут)"""
    scheduler = BackgroundScheduler()
    parser = ParserViewSet()
    scheduler.add_job(parser.main_parser,
                      "interval",
                      minutes=43200,
                      id=f"parser_{datetime.now().month}",
                      replace_existing=True)
    scheduler.start()
