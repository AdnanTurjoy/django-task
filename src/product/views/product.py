from django.views import generic
from rest_framework import viewsets
from product.models import Variant,Product,ProductVariant,Variant,ProductImage
from ..serializers import ProductSerializer,VariantSerializer,TotalVariantSerializer,ProductImageSerializer
from django.shortcuts import render,redirect
from multiprocessing import context
from rest_framework.filters import SearchFilter


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
# show Total Product
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends= [SearchFilter]
    search_fields = ['title']       # http://127.0.0.1:8000/api/Product/?search=dd

    # context={
       
    #     'data':queryset,
    # }
    

class CreateVariantView(viewsets.ModelViewSet):
     queryset = ProductVariant.objects.all()
     serializer_class = VariantSerializer

class VariantView(viewsets.ModelViewSet):
     queryset = Variant.objects.all()
     serializer_class = TotalVariantSerializer

class ProductImageView(viewsets.ModelViewSet):
     queryset = ProductImage.objects.all()
     serializer_class = ProductImageSerializer