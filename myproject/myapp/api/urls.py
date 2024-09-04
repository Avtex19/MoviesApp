from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', views.getRoutes),
    path('home/', Home.as_view(), name='home'),

]