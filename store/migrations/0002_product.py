# Generated by Django 4.2.1 on 2023-10-22 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='Страна')),
                ('brand', models.CharField(max_length=50, null=True, verbose_name='Бренд')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Название')),
                ('weight', models.CharField(max_length=10, null=True, verbose_name='Масса')),
                ('image', models.ImageField(null=True, upload_to='products_images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Цена')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Описание')),
                ('effect', models.CharField(max_length=50, null=True, verbose_name='Эффект')),
                ('application', models.CharField(max_length=256, null=True, verbose_name='Применение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategory')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]