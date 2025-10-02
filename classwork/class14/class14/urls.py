from django.contrib import admin
from django.urls import path, include
from certificates.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('certificates.urls')),  # App URLs under /certificates/
]
