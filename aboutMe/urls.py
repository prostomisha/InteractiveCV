from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test_yourself", views.test_yourself, name="test_yourself"),
    path("resume", views.resume, name="resume"),
]