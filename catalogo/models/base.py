"""
Modelos base/abstratos que podem ser herdados por outros modelos
"""
from django.db import models
from django.utils import timezone

class ModeloBase(models.Model):
    """
    Modelo abstrato com campos comuns a todos os modelos
    """
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Data de Criação"
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name="Última Atualização"
    )
    
    class Meta:
        abstract = True  # IMPORTANTE: não cria tabela no banco


class ModeloComSlug(models.Model):
    """
    Modelo abstrato para categorias/tags que precisam de slug
    """
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name="Slug",
        help_text="Identificador único para URLs"
    )
    
    class Meta:
        abstract = True