from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VendaSerializer, ItemVendaSerializer
from .models import Venda, ItemVenda
from core.views import BaseView
class VendasView(BaseView, ListCreateAPIView):
    queryset =  Venda.objects.all()
    serializer_class = VendaSerializer

class VendaView(BaseView, RetrieveUpdateDestroyAPIView):
    queryset =  Venda.objects.all()
    serializer_class = VendaSerializer
    
class ItensVendaView(BaseView, ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ItemVendaView(BaseView, RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer