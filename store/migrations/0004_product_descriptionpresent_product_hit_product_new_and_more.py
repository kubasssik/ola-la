# Generated by Django 4.2.1 on 2023-10-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_productcategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descriptionpresent',
            field=models.TextField(max_length=3000, null=True, verbose_name='Описание подарка'),
        ),
        migrations.AddField(
            model_name='product',
            name='hit',
            field=models.BooleanField(null=True, verbose_name='Хит'),
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(null=True, verbose_name='Новинка'),
        ),
        migrations.AddField(
            model_name='product',
            name='present',
            field=models.BooleanField(null=True, verbose_name='Подарок'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(max_length=3, null=True, verbose_name='Сумма скидки в процентах'),
        ),
    ]
