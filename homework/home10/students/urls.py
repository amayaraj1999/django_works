from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('students/search/', views.student_search, name='student_search'),
]
