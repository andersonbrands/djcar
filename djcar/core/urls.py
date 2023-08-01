from django.urls import path

from djcar.core import views

urlpatterns = [
    path("", views.home, name="home"),
]
