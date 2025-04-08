from rest_framework.serializers import ModelSerializer
from .models import Venda, ItemVenda

class VendaSerializer(ModelSerializer):
    
    class Meta:
        model = Venda
        fields = '__all__'
        
class ItemVendaSerializer(ModelSerializer):
    
    class Meta:
        model = ItemVenda
        fields = '__all__'