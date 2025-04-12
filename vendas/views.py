from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import VendaSerializer, ItemVendaSerializer
from .models import Venda, ItemVenda
from core.views import BaseView
from django.db.models import Sum
from rest_framework.response import Response

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

class EstatisticaVendasView(BaseView, APIView):
    
    def get(self, request):
        vendas_usuario = Venda.objects.filter(usuario=request.user).aaggregate(Sum('total'))['total__sum'] or 0
        return Response({"total_vendido": vendas_usuario})