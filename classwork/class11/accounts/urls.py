from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('visit/', views.visit_counter, name='visit'),
]

