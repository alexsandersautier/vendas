from django.db import models
from clientes.models import Cliente
from django.contrib.auth.models import User

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='vendas')
    data = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendas_usuario', blank=True, null=True) 
    
    def __str__(self):
        return self.cliente

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.CharField(max_length=255)
    quantidade = models.FloatField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()
    
    def __str__(self):
        return f"{self.venda} - {self.produto}"