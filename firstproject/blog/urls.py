from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog_list/', views.blog_list),
    path('blog_post/', views.blog_list),

]