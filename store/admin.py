from django.contrib import admin

from store.models import ProductCategory, Product


admin.site.register(ProductCategory)

@admin.register(Product)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('category', 'brand', 'name', 'weight', 'price')
    fields = ('category', 'brand', 'name',
               ('state', 'weight', 'price', 'quantity'),
                 'image', 'description', 'effect', 'application',
                   ('sale', 'salenum'), ('new', 'hit'), ('present', 'descriptionpresent'))

    
