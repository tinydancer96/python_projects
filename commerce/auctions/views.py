from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Category, Watchlist, Bids, Comments

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
    comments = Comments.objects.filter(listing=listing)
    message = request.GET.get('message', None)
    return render(request, ("auctions/view_listing.html"), {
        "listing": listing,
        "user": request.user,
        "comments": comments,
        "message": message
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
        user_id = request.user.id
        user= User.objects.get(pk=user_id)
        bid = Bids.objects.create(price=price, user=user)

        try:
            category, created = Category.objects.get_or_create(title=category_name)
            # user = request.user

            listing = Listing.objects.create(
                title=title,
                description=description,
                price=bid,
                user=user,
                image=image,
                categories=category
            )

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

def create_watchlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.POST.get('user')
            listing_id = request.POST.get('listing')

            user = User.objects.get(id=user_id)
            listing = Listing.objects.get(id=listing_id)

            watchlist, create = Watchlist.objects.get_or_create(user=user, listing=listing)
            if not create:
                message = f"{listing.title} is already in watchlist"
                return redirect(reverse("watchlist") + f"?message={message}")
            return redirect("watchlist")
        else:
            return render(request, "auctions/login.html")
    return render(request, "auctions/view_listing.html")

def watchlist(request):
    user = request.user
    message = request.GET.get('message', "")
    watchlist_index = Watchlist.objects.filter(user=request.user.id)
    return render(request, "auctions/watchlist.html", {
        "watchlist_index": watchlist_index,
        "message": message,
        "user": user
    })

def add_comment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('comment_title')
            description = request.POST.get('comment_description')
            user_id = request.POST.get('user_id')
            listing_id = request.POST.get('listing_id')

            user = User.objects.get(pk=user_id)
            listing = Listing.objects.get(pk=listing_id)
            comment = Comments.objects.create(title=title, description=description, user=user, listing=listing)
            return redirect("view_listing", listing_id)
        else:
            return redirect("login")
    return render(request, "auctions/view_listing.html")

def make_bid(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            listing_id = request.POST.get('listing_id')
            user_id = request.POST.get('user_id')
            price = request.POST.get('price')

            user = User.objects.get(pk=user_id)
            listing = Listing.objects.get(pk=listing_id)

            if float(listing.price.price) < float(price):
                bid = Bids.objects.create(price=price, user=user)
                listing.price = bid
                listing.save()
                message = "Bid Successful"
                return redirect(reverse("view_listing", kwargs={"listing_id":listing_id}) + f"?message={message}")
            else:
                message = "New bid must be greater than current bid"
                return redirect(reverse("view_listing", kwargs={"listing_id":listing_id}) + f"?message={message}")
        else:
            return redirect("login")
    return render(request, "auctions/view_listing.html")


def close_bid(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        user_id = request.POST.get('user_id')

        listing = Listing.objects.get(pk=listing_id)
        listing_user = listing.user
        user = User.objects.get(pk=user_id)
        if listing_user == user:
            listing.active = 'Closed'
            listing.save()
            return redirect(reverse("view_listing", kwargs={"listing_id":listing_id}))
    return render(request, "auctions/view_listing.html")
