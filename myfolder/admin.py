
from django.contrib import admin
from myfolder.models import Blog, News


# Register your models here.

class AdminBlog(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']

admin.site.register(Blog,AdminBlog)


class AdminNews(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_date', 'created_at']

admin.site.register(News,AdminNews)