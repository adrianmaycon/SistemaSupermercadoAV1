from django.shortcuts import render
from .models import Clientes
from .models import Produto
from datetime import datetime

def home(request):
    return render(request,'usuarios/home.html')

def clientes(request):
    # Salvar os dados do cliente no banco de dados
    novo_cliente = Clientes()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.cpf = request.POST.get('cpf')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.endereco = request.POST.get('endereco')
    novo_cliente.fone = request.POST.get('fone')
    novo_cliente.save()

    # Exibir os dados dos clientes cadastrados 
    clientes = {
        'clientes': Clientes.objects.all()
    }
    # Retornar os dados para a página de listagem de dados
    return render(request,'usuarios/usuarios.html',clientes)

def cadastrar_produto(request):
    #salvar
    novo_produto = Produto()
    novo_produto.cod_produto = request.POST.get('cod_produto'),
    novo_produto.nome = request.POST.get('nome'),
    novo_produto.descricao = request.POST.get('descricao'),
    novo_produto.preco = request.POST.get('preco'),
    novo_produto.categoria = request.POST.get('categoria'),
    novo_produto.quantidade = request.POST.get('quantidade'),
    novo_produto.fornecedor = request.POST.get('fornecedor'),
    novo_produto.validade = datetime.strptime(request.POST.get('validade'), '%Y-%m-%dT%H:%M')
    novo_produto.save()
    
def visualizar_clientes(request):
    # Exibir os dados dos clientes cadastrados 
    clientes = {
        'clientes': Clientes.objects.all()
    }
        # Retornar os dados para a página de listagem de dados
    return render(request,'usuarios/usuarios.html',clientes)


def cadastro_produto(request):
    return render(request, 'produtos/cadastro.html')

def cadastrar_produto(request):
    # Obtém o código do produto do formulário
    cod_produto = request.POST.get('cod_produto')
    # Verifica se já existe um produto com o mesmo código
    if Produto.objects.filter(cod_produto=cod_produto).exists(): 
        mensagem = 'Já existe um produto com este código.'
        # Se já existe um produto com o mesmo código, retorna uma mensagem de erro
        return render(request, 'produtos/cadastro.html', {'mensagem': mensagem})
        
    # Se o produto não existir cria uma instância de Produto com os dados do formulário
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome'),
    novo_produto.descricao = request.POST.get('descricao'),
    novo_produto.cod_produto = cod_produto,
    novo_produto.preco = request.POST.get('preco'),
    novo_produto.categoria = request.POST.get('categoria'),
    novo_produto.quantidade = request.POST.get('quantidade'),
    novo_produto.fornecedor = request.POST.get('fornecedor'),
    novo_produto.validade = datetime.strptime(request.POST.get('validade'), '%Y-%m-%dT%H:%M')
        
    # Salva o novo produto no banco de dados
    novo_produto.save()
    # Retorna uma mensagem de sucesso
    mensagem = 'Produto cadastrado com sucesso.'
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produtos/cadastro.html', {'mensagem': mensagem})


def visualizar_produtos(request):
    # Exibir os dados dos clientes cadastrados 
    produtos = {
        'produtos': Produto.objects.all()
    }
    return render(request,'produtos/produtos.html',produtos)