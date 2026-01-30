from django.db import models
from django.core.validators import MinValueValidator
from .base import ModeloBase
from .categoria import Categoria


class Produto(ModeloBase):
    """Modelo para produtos de acrílico"""
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,  # Impede excluir categoria com produtos
        related_name='produtos',
        verbose_name="Categoria"
    )
    
    codigo = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código",
        help_text="Código único do produto (ex: ACB-001)"
    )
    
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome do Produto"
    )
    
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição Detalhada"
    )
    
    # Atributos específicos para produtos de acrílico
    cor = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Cor",
        help_text="Ex: Transparente, Fumê, Rosa, Azul"
    )
    
    dimensoes = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Dimensões",
        help_text="Ex: 30x30cm, 25x25x25cm"
    )
    
    espessura = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Espessura",
        help_text="Ex: 3mm, 5mm, 8mm"
    )
    
    preco_custo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço de Custo",
        validators=[MinValueValidator(0)]
    )
    
    preco_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço de Venda",
        validators=[MinValueValidator(0)]
    )
    
    estoque = models.IntegerField(
        default=0,
        verbose_name="Quantidade em Estoque",
        validators=[MinValueValidator(0)]
    )
    
    estoque_minimo = models.IntegerField(
        default=5,
        verbose_name="Estoque Mínimo",
        validators=[MinValueValidator(0)]
    )
    
    destaque = models.BooleanField(
        default=False,
        verbose_name="Produto em Destaque"
    )
    
    imagem = models.ImageField(
        upload_to='produtos/%Y/%m/',  # Organiza por ano/mês
        blank=True,
        null=True,
        verbose_name="Foto do Produto"
    )
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['codigo']
        indexes = [
            models.Index(fields=['codigo']),
            models.Index(fields=['categoria', 'ativo']),
        ]
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    @property
    def margem_lucro(self):
        """Calcula a margem de lucro em porcentagem"""
        if self.preco_custo > 0:
            lucro = ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
            return round(lucro, 2)
        return 0.0
    
    @property
    def precisa_repor(self):
        """Verifica se o estoque está abaixo do mínimo"""
        return self.estoque <= self.estoque_minimo
    
    @property
    def status_estoque(self):
        """Retorna status do estoque com cores"""
        if self.estoque == 0:
            return ('Esgotado', 'danger')
        elif self.precisa_repor:
            return ('Baixo Estoque', 'warning')
        else:
            return ('Disponível', 'success')