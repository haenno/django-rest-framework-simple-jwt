# Create your views here.
import uuid

from faker import Faker
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from newsapi.models import News
from newsapi.serializers import NewsSerializer


class CreateFakeNewsAPIView(APIView):
    def get_queryset(self):
        return News.objects.all()

    def get_serializer(self, *args, **kwargs):
        return NewsSerializer(*args, **kwargs)

    def get(self, request, format=None):
        new_news = News()
        new_news.news_uuid = uuid.uuid4()
        new_news.assigned_to_uuid = uuid.uuid4()
        new_news.news_text = Faker().text(max_nb_chars=300)
        new_news.save()
        saved_news = self.get_queryset().filter(pk=new_news.pk).first()
        return Response(
            {
                "id": saved_news.pk,
                "news_uuid": saved_news.news_uuid,
                "created": saved_news.created,
                "assigned_to_uuid": saved_news.assigned_to_uuid,
                "news_text": saved_news.news_text,
            },
            status=201,
        )


class CreateNewsAPIView(CreateAPIView):
    model = News
    serializer_class = NewsSerializer

    def get_queryset(self):
        new_news = News()
        # new_news.news_uuid = uuid.uuid4()
        # new_news.assigned_to_uuid = uuid.uuid4()
        # new_news.news_text = Faker().text(max_nb_chars=300)
        # new_news.save()
        queryset = News.objects.filter(pk=new_news.pk)
        return queryset


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
