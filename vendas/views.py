from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VendaSerializer, ItemVendaSerializer
from .models import Venda, ItemVenda

class VendasView(ListCreateAPIView):
    queryset =  Venda.objects.all()
    serializer_class = VendaSerializer

class VendaView(RetrieveUpdateDestroyAPIView):
    queryset =  Venda.objects.all()
    serializer_class = VendaSerializer
    
class ItensVendaView(ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ItemVendaView(RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer