from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("mardgelle", views.mardgelle, name="mardgelle"),
    path("<str:name>", views.greet, name="greet")
]
