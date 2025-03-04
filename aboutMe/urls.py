from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test_yourself", views.test_yourself, name="test_yourself"),
    path("resume", views.resume, name="resume"),
    path("check_answer", views.check_answers, name="check_answers"),
    path("create_question", views.CreateQuestionView.as_view(), name="create_question"),
]