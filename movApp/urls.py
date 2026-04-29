from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="index"),
    path("newsletter/subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"),

]
