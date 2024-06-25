
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('onetoone/', include('onetoone.urls')),
    path('onetomany/', include('onetomany.urls')),
    path('manytomany/', include('manytomany.urls')),
]
