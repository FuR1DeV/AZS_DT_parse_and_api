from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from ..views import ParserViewSet


def scheduler_start():
    scheduler = BackgroundScheduler()
    parser = ParserViewSet()
    scheduler.add_job(parser.main_parser,
                      "interval",
                      minutes=1,
                      id=f"parser_{datetime.now().month}",
                      replace_existing=True)
    scheduler.start()
