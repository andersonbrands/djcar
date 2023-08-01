from django.urls import path

from djcar.core import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("add/", views.AddCarView.as_view(), name="add"),
]
