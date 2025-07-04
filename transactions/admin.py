# transactions/admin.py

from django.contrib import admin
from .models import Transaction, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'emoji', 'title')
    search_fields = ('title',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'type', 'date', 'category')
    list_filter = ('type', 'category', 'date')
    search_fields = ('title',)
    
    
admin.site.site_title = "Finance Admin"
admin.site.site_header = "Финансовый учёт"