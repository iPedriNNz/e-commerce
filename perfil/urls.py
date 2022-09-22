from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.CriarPerfil.as_view(), name="criar"),
    path('update/', views.AtualizarPerfil.as_view(), name="update"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
]
