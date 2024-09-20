
from django.contrib import admin
from app.models import Category, Link, Note

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass