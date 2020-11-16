from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("test3ds/", views.test3ds, name="form"),
    path("get_status/<str:transaction_id>", views.get_status, name="status")
]

