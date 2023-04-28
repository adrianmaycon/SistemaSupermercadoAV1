
from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsável, nome de referência
    #usuarios.com
    path('',views.home,name='home'),
    # usuarios.com/usuarios
    path('clientes/',views.clientes,name='listagem_clientes'),

    path('visualizar_clientes/',views.visualizar_clientes,name='visualizar_clientes'),


    path('produtos/cadastro', views.cadastro_produto, name='cadastro_produto'),


    path('produtos/produtos', views.cadastrar_produto, name='cadastrar_produto'),

    
    path('visualizar_produtos',views.visualizar_produtos, name='visualizar_produtos')
]
