"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve
from product.views.product import ProductView,CreateVariantView,VariantView,ProductImageView
from rest_framework import routers
from config import settings
from django.views.generic import TemplateView
route = routers.DefaultRouter()
route.register("api/Product",ProductView,basename='productView')
route.register("api/ProductVariant",CreateVariantView,basename='variantView')
route.register("api/Variant",VariantView,basename='totalVariantView')    
route.register("api/ProductImage",ProductImageView,basename='ProductImageView')  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('product/', include('product.urls')),
    path('product/', include(route.urls)),
    path('', include(route.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
