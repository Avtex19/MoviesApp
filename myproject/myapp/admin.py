from django.contrib import admin
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'genre', 'stars')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'movie')
