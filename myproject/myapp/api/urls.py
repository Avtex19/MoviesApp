from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.getRoutes),
    path('home/', Home.as_view(), name='home'),
    re_path(r'^users/$', UserList.as_view()),
    re_path(r'^create-users/$', UserCreate.as_view()),
    re_path(r'^genres/$', GenreListCreate.as_view()),
    re_path(r'^genres/(?P<pk>\d+)/$', GenreRetrieveUpdate.as_view()),

    re_path(r'^movies/$', MovieListCreate.as_view()),
    re_path(r'^movies/(?P<pk>\d+)/$', MovieRetrieveUpdate.as_view()),

    re_path(r'^comments/$', CommentListCreate.as_view()),
    re_path(r'^comments/(?P<pk>\d+)/$', CommentRetrieveUpdate.as_view())
]