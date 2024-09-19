from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Category, Link
from django.contrib.auth import authenticate, login, logout

def indexview(request):
    return render(request,'index.html')

def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'index.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')

    
def logout_action(request):
    logout(request)
    return render(request, 'index.html')

#Products
#Links

def linklistview(request):
    linklist = Link.objects.all()
    categorylist = Category.objects.all()
    context = {'links': linklist, 'categories': categorylist}
    return render(request,'linklist.html', context)

#Lisäys

def addlink(request):    
    a = request.POST['linkname']
    b = request.POST['link_link']
    c = request.POST['category']    
    Link(linkname = a, link_link = b, category = Category.objects.get(id = c)).save()
    return redirect(request.META['HTTP_REFERER'])

#Poisto
# Tätä funktiota kutsutaan ensin, kun poistetaan linkki. Se hakee linkin id:n perusteella ja lähettää sen confirmdelLink.html sivulle
# context nimet vapaasti nimettävissä
# Tässä esimerkissä on käytetty yksikkö muotoa link, koska on kyseessä yksi poistettava linkki
def confirmdeletelink(request, id):
    link = Link.objects.get(id = id)
    context = {'link': link}
    return render (request,"confirmdelLink.html",context)

def deletelink(request, id):
    Link.objects.get(id = id).delete()
    return redirect(reverse('links'))

#Editointi
def editlinkget(request, id):
    link = get_object_or_404(Link, id=id)
    categories = Category.objects.all()
    context = {'link': link, 'categories': categories}
    return render(request, 'editlink.html', context)


def editlinkpost(request, id):
    link = get_object_or_404(Link, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        link.linkname = request.POST['linkname']
        link.category_id = request.POST['category']
        link.link_link = request.POST['link_link']
        link.save()
        return redirect('links')
    return render(request, 'editlink.html', {'link': link, 'categories': categories})

'''
def editlinkget(request, id):
        link = Link.objects.get(id = id)
        context = {'link': link}
        return render (request,"editlink.html",context)
'''

'''
def editlinkpost(request, id):
        item = Link.objects.get(id = id)
        item.linkname = request.POST['linkname']
        item.category = request.POST['category']
        item.link_link = request.POST['link_link']
        item.save()
        return redirect(reverse('links'))'''

  
#Suppliers
#Categories

def categorylistview(request):
    categorylist = Category.objects.all()
    context = {'categories': categorylist}
    return render(request,'categorylist.html', context)

def addcategory(request):
    a = request.POST['categoryname']
    Category(categoryname = a).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletecategory(request, id):
    category = Category.objects.get(id = id)
    context = {'category': category}
    return render (request,"confirmdelCategory.html",context)

def deletecategory(request, id):
    Category.objects.get(id = id).delete()
    return redirect(reverse('categories'))
'''
def editcategoryget(request, id):
        category = Category.objects.get(id = id)
        context = {'category': category}
        return render (request,"editcategory.html",context)
'''

def editcategoryget(request, id):
    category = Category.objects.get(id=id)
    categorylist = Category.objects.all()  # Hae kaikki kategoriat dropdown-valikkoa varten
    context = {'category': category, 'categories': categorylist}
    return render(request, "editcategory.html", context)


def editcategorypost(request, id):
        item = Category.objects.get(id = id)
        item.categoryname = request.POST['categoryname']
        item.save()
        return redirect(reverse('categories'))

def searchcategories(request):
    search = request.POST['search']
    filtered = Category.objects.filter(categoryname__icontains=search)
    context = {'categories': filtered}
    return render (request,"categorylist.html",context)

def linksbycategory(request, id):
    category = get_object_or_404(Category, id=id)
    links = Link.objects.filter(category=category)  # Suodatetaan linkit kategorian mukaan
    context = {'category': category, 'links': links}
    return render(request, "linksbycategory.html", context)

'''
def linksbycategory(request):
    categorylist = Category.objects.get(id = id)
    context = {'categories': categorylist}
    return render (request,"categorylist.html",context)
'''

'''
def categorylistview(request):
    categorylist = Category.objects.all()
    context = {'categories': categorylist}
    return render(request,'categorylist.html', context)
'''


