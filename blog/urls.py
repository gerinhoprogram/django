# from django.contrib import admin
from django.urls import path
from . import views
# from django.http import HttpResponse
# from home import views as home_views
# from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/', views.post, name='post'),
    path('', views.blog, name='home'),
    
]