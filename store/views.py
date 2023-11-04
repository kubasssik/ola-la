from django.shortcuts import render
from store.models import Product, ProductCategory
from home.models import SettingSite
from django.core.paginator import Paginator

def products(request, pk=None):
    if pk:
        category = ProductCategory.objects.get(id=pk)
        product = Product.objects.filter(category=category)
    else:
        paginator = Paginator(Product.objects.order_by('-id'), 4)
        page_number = request.GET.get('page')
        product = paginator.get_page(page_number)
    context = {
        'title': 'Товары',
        'products': product,
        'categories': ProductCategory.objects.all(),  
        'settings': SettingSite.objects.all(),
        'is_hide': True
    }
    return render(request, 'store/products.html', context)




def product(request, pk):
    context = {
        'title': 'Товар', 
        'product': Product.objects.get(id=pk),
        'categories': ProductCategory.objects.all(), 
    }
    return render(request, 'store/product.html', context)      