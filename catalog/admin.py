from django.contrib import admin
from .models import Product, Brand, Category


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('owner', 'title')
    ordering = ['owner']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category')
    search_fields = ['title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)


