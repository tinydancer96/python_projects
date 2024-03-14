from django.contrib import admin
from .models import User, Listing, Category, Watchlist

# Register your models here.

class ListingInline(admin.TabularInline):
    model = Listing
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ListingInline]

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Watchlist)
# admin.site.register(Category)
