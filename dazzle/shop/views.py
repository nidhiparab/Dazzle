# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse


def index(request):

    allProds = []
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}

    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact")
    # return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("We are at tracker")
    # return render(request, 'shop/tracker.html')


def productview(request):
    return HttpResponse("We are at request")
    # return render(request, 'shop/prodview.html')


def search(request):
    # return render(request, 'shop/search.html')
    return HttpResponse("We are at search")


def checkout(request):
    return HttpResponse("We are at checkout")
    # return render(request, 'shop/checkout.html')
