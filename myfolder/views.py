from rest_framework import generics,permissions
from myfolder.models import Blog,News
from .serializer import BlogSerializer,NewsSerializer


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogAPIAdd(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Blog
    serializer_class = BlogSerializer


class BlogAPIDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Blog
    serializer_class = BlogSerializer



class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIAdd(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = News
    serializer_class = NewsSerializer


class NewsAPIDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = News
    serializer_class = NewsSerializer