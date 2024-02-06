from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("query/", views.query, name="query"),
    path("new_form", views.new_entry, name="new_entry")
]
