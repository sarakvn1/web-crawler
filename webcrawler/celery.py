# from __future__ import absolute_import
# import os
# from celery import Celery
#
# # set the default Django settings module for the 'celery' program.
# # from main.tasks import crawl_job
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcrawler.settings')
#
# # app = Celery('webcrawler', broker='amqp://guest@localhost//')
# app = Celery('webcrawler')
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings',namespace="CELERY")
# app.autodiscover_tasks()
# # app.conf.update(
# #     worker_max_tasks_per_child=1,
# #     broker_pool_limit=None
# # )
# # app.conf.task_routes = {'webcrawler.tasks.crawl': {'queue': 'crawl'}}
# #
#
# # app.conf.beat_schedule = {
# #     'add-every-30-seconds': {
# #         'task': 'main.tasks.crawl',
# #         'schedule': 20.0
# #     },
# # }
#
# @app.task(bind=True)
# def hello_world(self):
#     print('Hello world!')
#
#
# # @app.on_after_configure.connect
# # def setup_periodic_tasks(sender, **kwargs):
# #     # Calls test('hello') every 10 seconds.
# #     sender.add_periodic_task(1.0, test.s('hello'), name='add every 10')
# #
# #     # Calls test('world') every 30 seconds
# #     sender.add_periodic_task(2.0, test.s('world'), expires=10)
# #
# #     # Executes every Monday morning at 7:30 a.m.
# #     # sender.add_periodic_task(
# #     #     crontab(hour=7, minute=30, day_of_week=1),
# #     #     test.s('Happy Mondays!'),
# #     # )
# #
#
# # @app.task()
# # def crawl():
# #     crawl_job()
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'webcrawler.settings')

app = Celery('webcrawler',broker_url='redis://127.0.0.1:6379/0')

# app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


@app.task(bind=True)
def hello_world(self):
    print('Hello world!')