
from django.urls import path
from .views import indexview, linklistview, categorylistview, addcategory, addlink, \
    searchcategories, deletelink, confirmdeletelink,confirmdeletecategory, deletecategory, \
    editlinkget, editlinkpost, editcategoryget, editcategorypost, linksbycategory
 

urlpatterns = [
    path('', indexview),

    #Procucts
    #Links

    path('links/', linklistview , name='links'),
    path('add-link/', addlink, name='add-link'),
    path('confirm-delete-link/<int:id>/', confirmdeletelink, name='confirm-delete-link'),
    path('delete-link/<int:id>/', deletelink, name='delete-link'),
    path('edit-link-get/<int:id>/', editlinkget, name='edit-link-get'),
    path('edit-link-post/<int:id>/', editlinkpost, name='edit-link-post'),
    



    #Suppliers
    #Categories

    path('categories/', categorylistview, name='categories'),
    path('add-category/', addcategory, name='add-category'),
    path('confirm-delete-category/<int:id>/', confirmdeletecategory, name='confirm-delete-category'),
    path('delete-category/<int:id>/', deletecategory, name='delete-category'),
    path('edit-category-get/<int:id>/', editcategoryget, name='edit-category-get'),
    path('edit-category-post/<int:id>/', editcategorypost, name='edit-category-post'),
    path('search-categories/', searchcategories, name='search-categories'),
    path('links-by-category/<int:id>/', linksbycategory, name='links-by-category'),
    
    
    
    

    

]
