from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry>", views.entry, name="entry"),
    path("query/", views.query, name="query"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("encyclopedia/<str:entry>/edit", views.edit, name="edit")
]
