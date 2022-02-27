from django.urls import path
from main.views import Crawler

urlpatterns = [
    path('crawl', Crawler.as_view()),
]
