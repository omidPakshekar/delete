from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    return render(request,"home.html",{})

def about_view(request, *args, **kwargs):
    my_context = {
        "title" : "i am title",
        "mylist": [12,31,41]
    }
    return render(request,"about.html",my_context)
