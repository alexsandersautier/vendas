from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('vendas/', include('vendas.urls')),
    path('usuarios/', include('contas.urls')),
]
