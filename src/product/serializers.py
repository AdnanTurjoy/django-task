from rest_framework import serializers
from .models import Product,ProductVariant,Variant,ProductImage

class TotalVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model= Variant
        fields='__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductVariant
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    product=VariantSerializer(read_only=True,many=True)
    class Meta:
        model= Product
        fields='__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductImage
        fields='__all__'