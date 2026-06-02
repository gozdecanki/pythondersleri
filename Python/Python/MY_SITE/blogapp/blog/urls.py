

#http://127.0.0.1:8000/             => index
#http://127.0.0.1:8000/index        => index
#http://127.0.0.1:8000/blogs        => blogs
#http://127.0.0.1:8000/blogs/3      => blog-details

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index),
    path('blogs', views.blogs, name="blogs"),
    path('blogs/<int:id>', views.blog_details, name="blog_details"),
]
