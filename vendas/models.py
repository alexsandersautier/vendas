from django.db import models
from clientes.models import Cliente

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='vendas')
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Número: {self.pk} - Cliente: {self.cliente} - Emissão: {self.data.date()}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.CharField(max_length=255)
    quantidade = models.FloatField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()
    
    def __str__(self):
        return f"{self.venda} - {self.produto}"