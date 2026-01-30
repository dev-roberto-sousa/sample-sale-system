from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Produto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'icone', 
        'ordem', 
        'quantidade_produtos',
        'ativo', 
        'data_criacao'
    ]
    
    list_filter = ['ativo']
    search_fields = ['nome', 'descricao']
    prepopulated_fields = {'slug': ['nome']}
    ordering = ['ordem', 'nome']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'slug', 'descricao', 'icone')
        }),
        ('Configurações', {
            'fields': ('ordem', 'ativo')
        }),
    )


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 
        'nome', 
        'categoria',
        'preco_venda_formatado',
        'estoque_com_status',
        'ativo',
        'destaque'
    ]
    
    list_filter = [
        'categoria',
        'ativo',
        'destaque',
        'cor'
    ]
    
    search_fields = [
        'codigo',
        'nome',
        'descricao'
    ]
    
    list_editable = ['ativo', 'destaque']
    
    # Campos para exibição customizada
    def preco_venda_formatado(self, obj):
        return f"R$ {obj.preco_venda:.2f}"
    preco_venda_formatado.short_description = 'Preço Venda'
    
    def estoque_com_status(self, obj):
        status, cor = obj.status_estoque
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            cor,
            f"{obj.estoque} ({status})"
        )
    estoque_com_status.short_description = 'Estoque'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('categoria', 'codigo', 'nome', 'descricao')
        }),
        ('Especificações Técnicas', {
            'fields': ('cor', 'dimensoes', 'espessura'),
            'classes': ('collapse',)
        }),
        ('Preços e Estoque', {
            'fields': ('preco_custo', 'preco_venda', 'estoque', 'estoque_minimo')
        }),
        ('Status e Imagem', {
            'fields': ('ativo', 'destaque', 'imagem')
        }),
    )


# Registrar os modelos no admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)