from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/', views.list_notes, name='list_notes'),
]
