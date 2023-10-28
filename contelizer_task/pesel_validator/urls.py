from django.urls import path

from . import views


urlpatterns = [
    path("pesel/", views.pesel_validator_view, name="pesel")
    ]
