from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ListaDeProdutos')


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

