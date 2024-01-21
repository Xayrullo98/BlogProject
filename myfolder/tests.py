from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myfolder.models import *


class APITests(APITestCase):
    @classmethod
    def TestData(cls):
        cls.book = Blog.objects.create(
            title="Blog",
            content="Blog Api",
        )

    def testapi(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertContains(response, self.book)


class APITestNews(APITestCase):
    @classmethod
    def TestData(cls):
        cls.book = News.objects.create(
            title="News",
            content="News text",
            published_date='2024-01-21'
        )

    def testapi(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(News.objects.count(), 1)
        self.assertContains(response, self.book)