from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Category

def index(request):
    listings = Listing.objects.filter(active='Active')
    return render(request, "auctions/index.html", {
        "listings":  listings
        })


def my_listings(request):
    try:
        user = request.user
        listings = Listing.objects.filter(user=user)
    except:
        return render(request, "auctions/index.html")

    if listings is not None:
        return render(request, "auctions/my_listings.html", {
        "listings": listings
        })
    else:
        return render(request, "auctions/my_listings.html", {
        "message": "No listings available"
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def view_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, ("auctions/view_listing.html"), {
        "listing": listing
    })

def new_listing(request):
    return render(request, "auctions/new_listing.html")

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_name = request.POST.get('category')
        price = request.POST.get('price')
        image = request.POST.get('image')
        try:
            category, created = Category.objects.get_or_create(title=category_name)
            user = request.user

            listing = Listing.objects.create(
                title=title,
                description=description,
                price=price,
                user=user,
                image=image,
                categories=category
            )
            # listing.categories.add(category.title)

            return redirect("view_listing", listing_id=listing.id)
        except Exception as e:
            return render(request, "auctions/new_listing.html", {"error_message": str(e)})
    else:
        return render(request, "auctions/new_listing.html")


def categories(request):
    all_categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "list_categories": all_categories
    })

def view_category(request, category_id):
    category = Category.objects.get(id=category_id)
    listings = category.listings.all()
    return render(request, "auctions/view_category.html", {
        "category": category,
        "listings": listings
    })
