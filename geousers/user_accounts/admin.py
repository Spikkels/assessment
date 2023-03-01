from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Account


@admin.register(Account)
class ShopAdmin(OSMGeoAdmin):
    """Admin configuration for the Account model."""
    
    list_display = ('user', 'home_address', 'phone_number', 'location')
