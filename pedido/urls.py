from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name="pagar"),
    path('fecharpedido/', views.FecharPedido.as_view(), name="fechar"),
    path('detalhes/', views.DetalhesDoPedido.as_view(), name="detalhes"),
]
