from django.db import models

class SettingSite(models.Model):
    namesite = models.CharField('Название сайта', max_length=50, unique=True, blank=True)
    image = models.ImageField('Изображение описания', upload_to='site_images', null=True)
    descriptionsite = models.TextField('Описание сайта', max_length = 3000, null=True, blank=True) #Поле моет быть пустым, 
    phone = models.CharField('Телефон на сайте', max_length=15, blank=True)
    address = models.TextField('Адрес магазина', max_length = 500, null=True, blank=True)
    image_1 = models.ImageField('Фото-1', upload_to='site_images', null=True, blank=True)
    image_2 = models.ImageField('Фото-2', upload_to='site_images', null=True, blank=True)
    image_3 = models.ImageField('Фото-3', upload_to='site_images', null=True, blank=True)
    image_4 = models.ImageField('Фото-4', upload_to='site_images', null=True, blank=True)
    image_5 = models.ImageField('Фото-5', upload_to='site_images', null=True, blank=True)
    ip = models.CharField('Название ИП', max_length=50, null=True, blank=True )
    nameip = models.CharField('Имя руководителя', max_length=50, null=True )
    phonip = models.CharField('Телефон руководителя', max_length=15, blank=True)
    inn = models.CharField('ИНН', max_length=15, null=True )
    kpp = models.CharField('КПП', max_length=15, null=True )
    rs = models.CharField('р/с', max_length=50, null=True )
    bic = models.CharField('БИК', max_length=50, null=True )
    bank = models.CharField('Полное наименование банка, включая номер отделения или дополнительного офиса и город', max_length=256, null=True )
    ks = models.CharField('к/c', max_length=50, null=True )


    def __str__(self):
       return self.namesite #Для отображение название категории
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'
