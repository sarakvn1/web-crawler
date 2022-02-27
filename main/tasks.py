import os
import time
from pathlib import Path
from multiprocessing import Process, Queue, Pool

from twisted import runner
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from celery import shared_task
from celery.utils.log import get_task_logger
from crochet import setup
from crawler.spiders.tsetmc_main import TsetmcSpider
from crawler import settings as my_settings
from scrapy.settings import Settings
from subprocess import Popen, PIPE
from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler.spiders.tsetmc_main import TsetmcSpider

from django.core import management

# import scrapydo
#
# scrapydo.setup()


@shared_task(name="crawling task")
def crawl_task():
    try:
        management.call_command("scrapy", verbosity=0)
    except Exception as e:
        print(e)


# @shared_task(name="crawling task33")
# def crawl_task3():
#     spider = Popen(["scrapy", "crawl", "tsetmc"], stdout=PIPE)
#
#     spider.wait()


@defer.inlineCallbacks
def crawl77():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    c_runner = CrawlerRunner(crawler_settings)
    yield c_runner.crawl(TsetmcSpider)
    reactor.stop()

# @shared_task(name="scrapydo")
# def scrapydo1():
#     scrapydo.run_spider(TsetmcSpider)

@shared_task(name="scraping22")
def scrap():
    # if reactor.running:
    #     reactor.callFromThread(reactor.stop)
    if reactor.callWhenRunning(lambda: None) is not None:
        # reactor.stop()
        reactor.callFromThread(reactor.stop)
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    runner = CrawlerRunner(crawler_settings)
    d = runner.crawl(TsetmcSpider)
    # # d.addBoth(lambda _: reactor.stop())
    # print(f'sleeping for: 5sec')
    reactor.run()
    # process = CrawlerProcess(crawler_settings)
    # process.crawl(TsetmcSpider)

    # process.start(stop_after_crawl=False)
    print("sleeping for 1 sec")
    # time.sleep(1)

    # process.end()

def _crawl(spider_name=None):
    if spider_name:
        os.system('scrapy crawl %s' % spider_name)
    return None

@shared_task(name="cmd2")
def run_crawler():

    spider_names = ['tsetmc']
    pool = Pool(processes=len(spider_names))
    pool.map(_crawl, spider_names)


#
from scrapy import cmdline
@shared_task(name="cmd")
def crawl_cmd():

    cmdline.execute("scrapy crawl tsetmc".split())
#
# def sleep(_, duration=5):
#     print(f'sleeping for: {duration}')
#     time.sleep(duration)  # block here
#
#
@shared_task(name="scraping")
def loop_crawl():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    runner = CrawlerRunner(crawler_settings)
    crawl(runner)
    reactor.run()

#
# @shared_task(name="crawl")
# def run_spider():
#     def f(q):
#         try:
#             crawler_settings = Settings()
#             crawler_settings.setmodule(my_settings)
#             runner = CrawlerRunner(crawler_settings)
#             deferred = runner.crawl(TsetmcSpider)
#             deferred.addBoth(lambda _: reactor.stop())
#             reactor.run()
#             q.put(None)
#         except Exception as e:
#             q.put(e)
#
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     result = q.get()
#     p.join()
#
#     if result is not None:
#         raise result
