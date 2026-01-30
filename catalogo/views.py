from django.shortcuts import render
from .models import Categoria, Produto

def home(request):
    """View inicial do sistema"""
    total_categorias = Categoria.objects.filter(ativo=True).count()
    total_produtos = Produto.objects.filter(ativo=True).count()
    produtos_ativos = Produto.objects.filter(ativo=True).count()
    
    context = {
        'total_categorias': total_categorias,
        'total_produtos': total_produtos,
        'produtos_ativos': produtos_ativos,
    }
    return render(request, 'home.html', context)

def categoria_list(request):
    """Lista todas as categorias ativas"""
    categorias = Categoria.objects.all().order_by('ordem', 'nome')
    
    context = {
        'categorias': categorias,
    }
    return render(request, 'catalogo/categoria_list.html', context)