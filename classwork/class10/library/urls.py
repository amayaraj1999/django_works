from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_read, name='book_read'),                 
    path('books/paginated/', views.book_list_paginated, name='book_list_paginated'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:id>/', views.book_update, name='book_update'),
    path('books/delete/<int:id>/', views.book_delete, name='book_delete'),
]
