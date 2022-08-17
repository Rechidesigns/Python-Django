from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page(request):

    return HttpResponse("<h1>This is our home page</h1>")

def another_page(newpage):
    return HttpResponse("<h1>5 + 10 = 15</h1>")

def signup_page(request):
    return render(request, "signup.html")