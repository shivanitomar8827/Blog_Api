from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('Blog_list/', views.blog_list),
    # path('Blog_post/', views.blog_list),
    path('Blog_list/', views.Blogpost.as_view()),
    path('Blog_post/', views.Blogpost.as_view()),

] 