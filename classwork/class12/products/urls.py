from django.urls import path
from .views import add_product, get_products

urlpatterns = [
    path('products/', get_products, name='get_products'),     # GET API
    path('products/add/', add_product, name='add_product'),   # POST API
]
