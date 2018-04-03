from django.shortcuts import render, get_object_or_404
import json
from .models import Product, ProductDetail, Color, Size, Material
from django.http import HttpResponse
# Create your views here.


# def product_detail(request):
#     products = Product.objects.all()
#     return render(request, 'case/index.html', {'products': products})


def index(request):
    products = Product.objects.all()

    return render(request, 'case/index.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_det = ProductDetail.objects.filter(product=product)
    # colors = Color.objects.productdetail_set.all().values_list('name', flat=True)
    colors = [product_detail.color.name for product_detail in product_det]
    sizes = [product_detail.size.name for product_detail in product_det]
    materials = [product_detail.material.name for product_detail in product_det]

    return render(request, 'case/test.html', {'product': product,
                                              'product_det': product_det,
                                              'colors': list(set(colors)),
                                              'sizes': list(set(sizes)),
                                              'materials': list(set(materials))
                                              })


def color_price(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod')
        color_a = request.GET.get('color')
        prod_det = ProductDetail.objects.filter(product=prod_id, color__name=color_a)
        price_det = prod_det.values_list('price', flat=True)
        a = 0
        for i in price_det:
              a += i

        return HttpResponse(json.dumps({
            "price": str(a), }),
            content_type="application/json")



