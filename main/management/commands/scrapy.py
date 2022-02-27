from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.tsetmc_main import TsetmcSpider
from crawler import settings as my_settings
from scrapy.settings import Settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(get_project_settings())
        process.crawl(TsetmcSpider)
        process.start()
        process.stop()
