from django.contrib import admin
from django.urls import path, include

'''Päätason Urlit'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')) # Tämä ohjaa kaikki pyynnöt app/urls.py:lle
]
