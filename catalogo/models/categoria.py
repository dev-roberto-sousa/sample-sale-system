from django.db import models
from django.utils.text import slugify
from .base import ModeloBase, ModeloComSlug


class Categoria(ModeloBase, ModeloComSlug):
    """Modelo para categorias de produtos (Boleiras, Mesas, Cubos...)"""
    
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da Categoria"
    )
    
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição",
        help_text="Descreva brevemente esta categoria"
    )
    
    ordem = models.IntegerField(
        default=0,
        verbose_name="Ordem",
        help_text="Número para ordenar as categorias (menor vem primeiro)"
    )
    
    # Campo para imagem/ícone da categoria (opcional)
    icone = models.CharField(
        max_length=50,
        blank=True,
        default="bi-tag",
        verbose_name="Ícone",
        help_text="Classe do Bootstrap Icons (ex: bi-tag, bi-box, bi-cup)"
    )
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['ordem', 'nome']
    
    def save(self, *args, **kwargs):
        """Gera o slug automaticamente se não existir"""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome
    
    @property
    def quantidade_produtos(self):
        """Retorna quantidade de produtos nesta categoria"""
        from .produto import Produto  # Import aqui para evitar circular
        return self.produtos.count()