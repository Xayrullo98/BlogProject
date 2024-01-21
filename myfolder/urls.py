from django.urls import path
from .views import *
urlpatterns = [
    path("", BlogAPIView.as_view(), name="blog"),
    path("add/", BlogAPIAdd.as_view(), name="blog_add"),
    path("change/<pk>/", BlogAPIDeleteUpdate.as_view(), name="blog_change"),
    path("news/", NewsAPIView.as_view(), name="news"),
    path("add/", NewsAPIAdd.as_view(), name="news_add"),
    path("change_news/<pk>/", NewsAPIDeleteUpdate.as_view(), name="news_change"),
]