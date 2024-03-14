from django.urls import path
from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:entry>", views.entry, name="entry"),
    path("error/", views.error, name="error"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("search", views.search, name="search"),
    path("<str:entry>/edit", views.edit, name="edit"),
    path("<str:entry>/save_edit/", views.save_edit, name="save_edit"),
    path("random/", views.random_entry, name="random_entry")
]
