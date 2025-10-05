from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # Home page
    path('add_teacher/', views.add_teacher, name='add_teacher'),
]
