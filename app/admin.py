
from django.contrib import admin
from app.models import Category, Link

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


