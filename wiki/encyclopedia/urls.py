from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("entries/<str:entry>", views.entry, name="entry"),
    path("query/", views.query, name="query"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit")
]
