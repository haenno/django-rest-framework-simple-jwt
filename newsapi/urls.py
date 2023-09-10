import uuid

from django.urls import path
from faker import Faker

from newsapi.models import News
from newsapi.views import LatestNewsListAPIView, NewsAfterIdListAPIView

# create 30 news on each startup
for _ in range(30):
    new_news = News()
    new_news.news_uuid = uuid.uuid4()
    new_news.assigned_to_uuid = uuid.uuid4()
    new_news.news_text = Faker().text(max_nb_chars=300)
    new_news.save()


app_name = "newsapi"

urlpatterns = [
    path("latest_news/", LatestNewsListAPIView.as_view(), name="latest_news"),
    path(
        "news_after_id/<int:news_id>/",
        NewsAfterIdListAPIView.as_view(),
        name="latest_news",
    ),
]
