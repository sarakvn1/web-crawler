import scrapy
from scrapy_djangoitem import DjangoItem
from main.models import Index, IndexInfluence, PopularIndex


class IndexItem(DjangoItem):
    django_model = Index


class IndexInfluenceItem(DjangoItem):
    django_model = IndexInfluence


class PopularIndexItem(DjangoItem):
    django_model = PopularIndex
