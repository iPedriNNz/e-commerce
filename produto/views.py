from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalhesDoProduto')



class AdiocionarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AddCarrinho')



class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RmvCaarrinho')



class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')



class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')

