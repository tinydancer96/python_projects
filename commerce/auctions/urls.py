from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.view_listing, name="view_listing"),
    path("my_listings", views.my_listings, name="my_listings"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("create", views.create, name="create"),
    path("categories", views.categories, name="categories"),
    path("view_category/<int:category_id>", views.view_category, name="view_category")
]
