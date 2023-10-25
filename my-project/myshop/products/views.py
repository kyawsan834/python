from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    userName = "hay"
    products = 4
    return render(request,"products/home.html",{
        "username" : userName,
        "product" : products,
    })



def signup(request):
    return render(request,"products/signup.html");



def product(request, product):
    if (product=="suits" or product=="dresses" or product=="shirts" or product == "shoes" ):
        return HttpResponse(f"{product} page")
    else:
        return HttpResponse(f"Page not found")
