
from django.urls import path
from .views import landingview, linklistview, categoryview

urlpatterns = [
    path('', landingview),

    #Links
    path('links/', linklistview),

    #Categories
    path('categories/', categoryview),
]
