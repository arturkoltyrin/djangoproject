from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def catalog(request):
    return render(request, 'catalog/catalog.urls')