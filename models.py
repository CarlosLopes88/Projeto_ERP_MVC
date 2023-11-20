#Models

from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Vendas:
    def __init__(self, itensvendidos: Produtos, vendedor, comprador, quantidadevendida, valorvendido, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensvendidos = itensvendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadevendida = quantidadevendida
        self.valorvendido = valorvendido
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, endereco, telefone, email):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.email = email  

class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, email, idfuncionario, cargo, salario):
        self.idfuncionario = idfuncionario
        self.salario = salario
        self.cargo = cargo
        super(Funcionario, self).__init__(nome, cpf, telefone, endereco, email)

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, email, idcliente):
        self.idcliente = idcliente
        super(Cliente, self).__init__(nome, cpf, telefone, endereco, email)