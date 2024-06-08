from django.contrib import admin
from .models import Blog, Like, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_link = ('id', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)
    list_display_links = ('id', 'author')