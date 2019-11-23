"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomeView, ReleaseView, InfoView, RecordListView, CourseListView, ContentView, CommentView,TimeView,GbookView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^release/', ReleaseView.as_view(), name='release'),
    url(r'^info/(?P<blog_id>\d+$)', InfoView.as_view(), name='info'),
    url(r'^recordlist/', RecordListView.as_view(), name='recordlist'),
    url(r'^courselist/', CourseListView.as_view(), name='courselist'),
    url(r'^content/(?P<blog_id>\d+$)', ContentView.as_view(), name='content'),
    url(r'^comment$', CommentView.as_view(), name='comment'),
    url(r'^time/', TimeView.as_view(), name='time'),
    url(r'^gbook/', GbookView.as_view(), name='gbook'),
]
