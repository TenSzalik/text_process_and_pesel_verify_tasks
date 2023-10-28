from django.urls import path

from . import views

urlpatterns = [
    path("process_text/", views.word_processing_view, name="process_text")
    ]
