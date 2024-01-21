from rest_framework import serializers
from myfolder.models import Blog, News


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id","title", "content", "created_at", )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id",'title', "content","published_date", "created_at", )