
from django.urls import path
from .views import landingview, linklistview, categorylistview, addcategory, addlink

urlpatterns = [
    path('', landingview),

    #Procucts
    #Links

    path('links/', linklistview),
    path('add-link/', addlink, name='add-link'),


    #Suppliers
    #Categories

    path('categories/', categorylistview, name='categories'),
    path('add-category/', addcategory, name='add-category'),
    path('search-categories/', categorylistview, name='search-categories'),
    
    

    

]
