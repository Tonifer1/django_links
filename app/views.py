from django.shortcuts import render

def landingview(request):
    return render(request,'landingpage.html')

def linklistview(request):
    return render(request,'linklist.html')

def categoryview(request):
    return render(request,'categorylist.html')


