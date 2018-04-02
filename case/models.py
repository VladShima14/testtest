from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Color(ProductAttribute):
    pass


class Size(ProductAttribute):
    pass


class Material(ProductAttribute):
    pass


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name='productdetail', verbose_name='Товар')
    color = models.ForeignKey(Color, related_name='colordetail', verbose_name='Цвет товара')
    size = models.ForeignKey(Size, related_name='sizedetail', verbose_name='Размер товара')
    material = models.ForeignKey(Material, related_name='materialdetail', verbose_name='Материал товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
