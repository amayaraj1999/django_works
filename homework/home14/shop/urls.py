from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/pdf/', views.product_pdf, name='product_pdf'),
    path('product/<int:pk>/email/', views.send_product_email, name='send_product_email'),
]
