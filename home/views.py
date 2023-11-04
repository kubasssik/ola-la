from django.shortcuts import render
from store.models import Product, ProductCategory
from home.models import SettingSite

def index(request):
    context = {
        'title': 'Главная страница', 
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),  
        'settings': SettingSite.objects.all(), 
    }
    return render(request, 'home/index.html', context)
