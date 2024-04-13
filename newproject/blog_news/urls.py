
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('news/', views.news, name='blog-news'),
    
]