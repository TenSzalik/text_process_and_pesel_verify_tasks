from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index_view),
    path("", include("word_processing.urls")),
    path("", include("pesel_validator.urls")),
]
