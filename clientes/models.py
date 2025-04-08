from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome