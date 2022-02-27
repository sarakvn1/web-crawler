from twisted.internet import reactor
# Create your views here.
from rest_framework.views import APIView
# from main.tasks import crawl

from rest_framework.response import Response
# from webcrawler.celery import
class Crawler(APIView):

    def get(self, request):
        # crawl.delay()
        print("hi")
        return Response("success.")
