from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.product_detail, name='test_detail'),
    url(r'^colorprice/', views.color_price, name='product_price')

]
