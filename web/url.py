from django.conf.urls import url
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^$', views.index, name='list'),
]
