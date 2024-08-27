from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from apps.base.models import BaseModel
from django.urls import reverse

class Fornecedor(BaseModel):
    TIPO_FORNECEDOR_CHOICE = [
        ("CPF", "CPF"),
        ("CNPJ", "CNPJ"),
    ]
    tipo = models.CharField('Tipo', max_length=4, choices=TIPO_FORNECEDOR_CHOICE, default="CNPJ")
    nome = models.CharField('Nome', max_length=200)
    documento = models.CharField('Documento', max_length=50, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    class Meta:
        verbose_name = 'Fornecedo'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']

    def __str__(self):
        return self.nome