from django.db import models


class ProductCategory(models.Model):
    category = models.CharField('Название категории', max_length=40, unique=True)
    description = models.TextField('Описание', max_length = 3000, null=True, blank=True) #Поле моет быть пустым, 
    image = models.ImageField('Изображение', upload_to='category_images', null=True)
    
    def __str__(self):
       return self.category #Для отображение название категории
    
     
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        
    

class Product(models.Model):
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    brand = models.CharField('Бренд *', max_length = 50, null=True)
    name = models.CharField('Название *', max_length= 256, null=True)
    state = models.CharField('Страна *', max_length = 50, null=True)
    weight = models.CharField('Масса *', max_length = 10, null=True)
    image = models.ImageField('Изображение: максимум 2000*2000', upload_to='products_images', null=True)
    quantity = models.PositiveIntegerField('Остаток на складе', default=0)
    price = models.DecimalField('Цена *', max_digits=8, decimal_places=2, null=True)#Ограничение по цене
    sale = models.BooleanField('Скидка', null=True, blank=True )
    salenum = models.CharField('Сумма скидки в процентах (без символа %)', max_length = 3, null=True, blank=True)
    new = models.BooleanField('Новинка', null=True, blank=True )
    hit = models.BooleanField('Хит', null=True, blank=True )
    present = models.BooleanField('Подарок', null=True, blank=True)
    descriptionpresent = models.TextField('Описание подарка', max_length = 3000, null=True, blank=True)
    description = models.TextField('Описание *', max_length=3000, null=True)
    effect = models.CharField('Эффект *', max_length = 50, null=True)
    application = models.CharField('Применение *', max_length = 256, null=True)
    
    def __str__(self):
        return f'Товар: {self.name} | Категория: {self.category.category}'
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

  



 #PROTECT - Не удалит категорию, пока все товары не удалят в ней
 #CASCADE - удаляет всю категорию со всеми товарами
 #SET_DEFAULT, default='' - если удалить, будет дефолтное название категории+
