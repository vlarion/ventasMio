from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mantenedores/', include('mantenedor.urls')),
    path('', include('django.contrib.auth.urls')),
]
