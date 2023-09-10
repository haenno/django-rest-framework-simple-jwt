import uuid

from django.urls import path
from faker import Faker

from newsapi.models import News
from newsapi.views import (
    CreateFakeNewsAPIView,
    CreateNewsAPIView,
    LatestNewsListAPIView,
    NewsAfterIdListAPIView,
)

app_name = "newsapi"

urlpatterns = [
    path("fake_news/", CreateFakeNewsAPIView.as_view()),
    path("create_news/", CreateNewsAPIView.as_view(), name="create_news"),
    path("latest_news/", LatestNewsListAPIView.as_view(), name="latest_news"),
    path(
        "news_after_id/<int:news_id>/",
        NewsAfterIdListAPIView.as_view(),
        name="latest_news",
    ),
]
