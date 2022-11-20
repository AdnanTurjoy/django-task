from django.views import generic
from rest_framework import viewsets
from product.models import Variant,Product,ProductVariant
from ..serializers import ProductSerializer,VariantSerializer
from django.shortcuts import render,redirect
from multiprocessing import context

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
    context={
       
        'data':queryset,
    }
    

class CreateVariantView(viewsets.ModelViewSet):
     queryset = ProductVariant.objects.all()
     serializer_class = VariantSerializer
     