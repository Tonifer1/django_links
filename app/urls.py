
from django.urls import path
from .views import landingview, linklistview, categorylistview, addcategory, addlink, \
    searchcategories, deletelink, confirmdeletelink,confirmdeletecategory, deletecategory
 

urlpatterns = [
    path('', landingview),

    #Procucts
    #Links

    path('links/', linklistview , name='links'),
    path('add-link/', addlink, name='add-link'),
    path('confirm-delete-link/<int:id>/', confirmdeletelink, name='confirm-delete-link'),
    path('delete-link/<int:id>/', deletelink, name='delete-link'),
    



    #Suppliers
    #Categories

    path('categories/', categorylistview, name='categories'),
    path('add-category/', addcategory, name='add-category'),
    path('search-categories/', searchcategories, name='search-categories'),
    path('confirm-delete-category/<int:id>/', confirmdeletecategory, name='confirm-delete-category'),
    path('delete-category/<int:id>/', deletecategory, name='delete-category'),
    
    

    

]
