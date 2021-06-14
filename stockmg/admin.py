from django.contrib import admin
from .models import *
from .forms import StockCreateForm



class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
    search_fields = ['category', 'item_name']
    list_filter = ['category']

# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)