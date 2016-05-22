from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from ui import views

urlpatterns = [    
    url(r'^project/(?P<page_slug>[\w-]+)', views.project_dashboard),
    url(r'^repo/(?P<page_slug>[\w-]+)', views.repo_dashboard),    
    url(r'^repo/(?P<page_slug>[\w-]+)/smells', views.smells),
    url(r'^leaderboard/', views.leaderboard),
    url(r'^wall-0f-shame/', views.wall_of_shame),
    url(r'^', views.dashboard),
]