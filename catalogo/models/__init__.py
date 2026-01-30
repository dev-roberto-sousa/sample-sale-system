"""
Este arquivo é CRUCIAL: ele expõe os models para o Django
"""
from .categoria import Categoria
from .produto import Produto

# Lista todos os models disponíveis
__all__ = ['Categoria', 'Produto']