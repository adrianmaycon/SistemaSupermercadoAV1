from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cpf = models.TextField(max_length=16)
    email = models.TextField(max_length=100)
    endereco = models.TextField(max_length=255)
    fone = models.TextField(max_length=20)

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    cod_produto = models.TextField(max_length=255)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco  = models.TextField(max_length=255)
    categoria = models.TextField(max_length=255)
    quantidade = models.TextField(max_length=255)
    fornecedor = models.TextField(max_length=255)
    validade = models.DateTimeField()
