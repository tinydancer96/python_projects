from django.urls import path
from . import views
from . import util

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:entry>", views.entry, name="entry")
]
