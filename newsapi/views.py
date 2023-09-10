# Create your views here.
import uuid

from faker import Faker
from rest_framework.generics import CreateAPIView, ListAPIView

from newsapi.models import News
from newsapi.serializers import NewsSerializer


class CreateNewsAPIView(CreateAPIView):
    model = News
    serializer_class = NewsSerializer

    def get_queryset(self):
        new_news = News()
        new_news.news_uuid = uuid.uuid4()
        new_news.assigned_to_uuid = uuid.uuid4()
        new_news.news_text = Faker().text(max_nb_chars=300)
        new_news.save()
        return new_news


class LatestNewsListAPIView(ListAPIView):
    model = News
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by("-created")[:10]


class NewsAfterIdListAPIView(ListAPIView):
    lookup_url_kwarg = "news_id"
    model = News
    serializer_class = NewsSerializer

    def get_queryset(self):
        news_id = self.kwargs.get(self.lookup_url_kwarg)
        news_after_id = News.objects.filter(pk__gt=news_id).order_by("-created")
        return news_after_id
