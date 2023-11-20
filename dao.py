#Data Access Object

from models import *

class DaoCategoria:
    @classmethod
    def save(cls, categoria):
        with open('categorias.txt', 'a') as file:
            file.write(f'{categoria}\n')

    @classmethod
    def read(cls):
        with open('categorias.txt', 'r') as file:
            cls.categorias = file.readlines()

            cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categorias))
  
            categoria_list = []
            for i in cls.categoria:
                categoria_list.append(Categoria(i))
            return categoria_list

class DaoVendas:
    @classmethod
    def save(cls, venda: Vendas):
        with open('vendas.txt', 'a') as file:
            file.write(f'{venda.itensvendidos.nome}|{venda.itensvendidos.preco}|{venda.itensvendidos.categoria}|{venda.vendedor}|{venda.comprador}|{venda.quantidadevendida}|{venda.valorvendido}|{venda.data}\n')

    @classmethod
    def read(cls):
        with open('vendas.txt', 'r') as file:
            cls.venda = file.readlines()

            cls.venda = [line.strip() for line in cls.venda]

            cls.venda = list(map(lambda x: x.split('|'), cls.venda))

            venda_list = []
            for i in cls.venda:
                if len(i) >= 6:  # Ajuste aqui para garantir que há informações suficientes
                    venda_list.append(Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return venda_list

class DaoEstoque:
    @classmethod
    def save(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as file:
            file.write(f'{produto.nome}|{produto.preco}|{produto.categoria}|{quantidade}\n')

    @classmethod
    def read(cls):
        with open('estoque.txt', 'r') as file:
            cls.estoque = file.readlines()

            cls.estoque = [line.strip() for line in cls.estoque]

            cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

            estoque_list = []
            for i in cls.estoque:
                if len(i) > 0:
                    estoque_list.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
            return estoque_list

class DaoFornecedor:
    @classmethod
    def save(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as file:
            file.write(f'{fornecedor.nome}|{fornecedor.cnpj}|{fornecedor.endereco}|{fornecedor.telefone}|{fornecedor.email}\n')

    @classmethod
    def read(cls):
        with open('fornecedores.txt', 'r') as file:
            cls.fornecedores = file.readlines()

            cls.fornecedores = [line.strip() for line in cls.fornecedores]

            cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

            fornecedores_list = []
            for i in cls.fornecedores:
                if len(i) > 0:
                    fornecedores_list.append(Fornecedor(i[0], i[1], i[2], i[3], i[4]))
            return fornecedores_list

class DaPessoa:
    @classmethod
    def save(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as file:
            file.write(f'{pessoa.nome}|{pessoa.cpf}|{pessoa.telefone}|{pessoa.endereco}|{pessoa.email}\n')

    @classmethod
    def read(cls):
        with open('pessoas.txt', 'r') as file:
            cls.pessoas = file.readlines()

            cls.pessoas = [line.strip() for line in cls.pessoas]

            cls.pessoas = list(map(lambda x: x.split('|'), cls.pessoas))

            pessoas_list = []
            for i in cls.pessoas:
                if len(i) > 0:
                    pessoas_list.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
            return pessoas_list

class DaoCliente:
    @classmethod
    def save(cls, cliente: Cliente):
        with open('clientes.txt', 'a') as file:
            file.write(f'{cliente.nome}|{cliente.cpf}|{cliente.telefone}|{cliente.endereco}|{cliente.email}|{cliente.idcliente}\n')

    @classmethod
    def read(cls):
        with open('clientes.txt', 'r') as file:
            cls.clientes = file.readlines()

            cls.clientes = [line.strip() for line in cls.clientes]

            cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

            clientes_list = []
            for i in cls.clientes:
                if len(i) > 0:
                    clientes_list.append(Cliente(i[0], i[1], i[2], i[3], i[4], i[5]))
            return clientes_list

class DaoFuncionario:
    @classmethod
    def save(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as file:
            file.write(f'{funcionario.nome}|{funcionario.cpf}|{funcionario.telefone}|{funcionario.endereco}|{funcionario.email}|{funcionario.idfuncionario}|{funcionario.cargo}|{funcionario.salario}\n')

    @classmethod
    def read(cls):
        with open('funcionarios.txt', 'r') as file:
            cls.funcionarios = file.readlines()

            cls.funcionarios = [line.strip() for line in cls.funcionarios]

            cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

            funcionarios_list = []
            for i in cls.funcionarios:
                if len(i) > 0:
                    funcionarios_list.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            return funcionarios_list