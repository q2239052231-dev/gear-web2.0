from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'product_type', 'created_at', 'is_handled']
    list_filter = ['is_handled', 'created_at']
    search_fields = ['name', 'phone', 'product_type', 'demand']
    list_per_page = 20
    ordering = ['-created_at']
