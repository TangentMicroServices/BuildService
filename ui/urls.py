from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from ui import views

urlpatterns = [    
    url(r'^project/(?P<project>[\w-]+)', views.project_dashboard, name='project_dashboard'),
    url(r'^repo/(?P<repo>[\w-]+)', views.repo_dashboard, name='repo_dashboard'),    
    url(r'^repo/(?P<repo>[\w-]+)/smells', views.smells, name='smells'),
    url(r'^leaderboard/', views.leaderboard, name='leaderboard'),
    url(r'^wall-0f-shame/', views.wall_of_shame, name='wall_of_shame'),
    url(r'^', views.dashboard, name='overview_dashboard'),
]