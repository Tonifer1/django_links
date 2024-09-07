from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Category, Link

def landingview(request):
    return render(request,'landingpage.html')

#Products
#Links

def linklistview(request):
    linklist = Link.objects.all()
    categorylist = Category.objects.all()
    context = {'links': linklist, 'categories': categorylist}
    return render(request,'linklist.html', context)

def addlink(request):    
    a = request.POST['linkname']
    b = request.POST['link_link']
    c = request.POST['category']    
    Link(linkname = a, link_link = b, category = Category.objects.get(id = c)).save()
    return redirect(request.META['HTTP_REFERER'])



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

def searchcategories(request):
    search = request.POST['search']
    filtered = Category.objects.filter(categoryname__icontains=search)
    context = {'categories': filtered}
    return render (request,"categorylist.html",context)


