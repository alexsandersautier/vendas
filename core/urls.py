from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticar/', include('autenticacao.urls')),
    path('clientes/', include('clientes.urls')),
    path('usuarios/', include('contas.urls')),
    path('vendas/', include('vendas.urls')),
]
