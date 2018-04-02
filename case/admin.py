from django.contrib import admin
from .models import Product, Color, Size, Material, ProductDetail

# Register your models here.


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'size', 'material', 'price']


class ProductDetailInstance(admin.TabularInline):
    model = ProductDetail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductDetailInstance]


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Material)
admin.site.register(ProductDetail, ProductDetailAdmin)
