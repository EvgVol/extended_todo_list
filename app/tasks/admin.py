from django.contrib import admin
from .models import Category, Task


@admin.register(Task)
class TastAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'user']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
