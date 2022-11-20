from django.contrib import admin
from .models import Product,ProductVariant,Variant
# Register your models here.

admin.site.register(Variant)
admin.site.register(ProductVariant)
admin.site.register(Product)
