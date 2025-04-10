from rest_framework.serializers import ModelSerializer
from .models import Venda, ItemVenda

class ItemVendaSerializer(ModelSerializer):
    
    class Meta:
        model = ItemVenda
        fields = '__all__'
class VendaSerializer(ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)
    class Meta:
        model = Venda
        fields = ['cliente', 'data', 'itens']