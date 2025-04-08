from django.urls import path
from .views import VendasView, VendaView, ItemVendaView, ItensVendaView

urlpatterns = [
    path('', view=VendasView.as_view(), name='vendas'),
    path('<int:pk>/', view=VendaView.as_view(), name='venda'),
    path('itens/', view=ItensVendaView.as_view(), name='itens'),
    path('itens/<int:pk>/', view=ItemVendaView.as_view(), name='item'),
]