import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeapp.settings')

app = Celery('financeapp',  broker="amqp://rabbit:rabbit@rabbitmq:5672//")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='celery')

# Scrape the database every 1h
scrape_periodic_interval = 60 * 60

app.conf.beat_schedule = {
    'scrape_aapl': {
        'task': 'news.tasks.scrape_yahoo_finance_rss',
        'schedule': scrape_periodic_interval,
        'args': ('AAPL',)
    },
    'scrape_twtr': {
        'task': 'news.tasks.scrape_yahoo_finance_headline',
        'schedule': scrape_periodic_interval,
        'args': ('TWTR',)
    },
    'scrape_gcgold': {
        'task': 'news.tasks.scrape_yahoo_finance_headline',
        'schedule': scrape_periodic_interval,
        'args': ('GC=F',)
    },
    'scrape_intc': {
        'task': 'news.tasks.scrape_yahoo_finance_headline',
        'schedule': scrape_periodic_interval,
        'args': ('INTC',)
    },
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

