from django.urls import path
from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:entry>", views.entry, name="entry"),
    path("error/", views.error, name="error"),
    path("new_entry", views.new_entry, name="new_entry")
    # path("update/<str:entry>", views.update, name="update")
]
