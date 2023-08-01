from django.urls import path

from djcar.core import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]
