from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            engine = create_engine(CONN, echo=True)
            Session = sessionmaker(bind=engine)
            cls._instance.session = Session()
        return cls._instance

def conectar_db():
    return Database().session

class DaoCategoria:
    @classmethod
    def save(cls, categoria: Categoria, session=None):
        if not session:
            session = conectar_db()
        session.add(categoria)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Categoria).all()

    @classmethod
    def delete(cls, categoria: Categoria, session=None):
        if not session:
            session = conectar_db()
        session.delete(categoria)
        session.commit()

    @classmethod
    def update(cls, categoria_antiga: Categoria, categoria_nova: Categoria, session=None):
        if not session:
            session = conectar_db()
        categoria_antiga.categoria = categoria_nova.categoria
        session.commit()

class DaoVendas:
    @classmethod
    def save(cls, venda: Vendas, session=None):
        if not session:
            session = conectar_db()
        session.add(venda)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Vendas).all()
    
    @classmethod
    def delete(cls, venda: Vendas, session=None):
        if not session:
            session = conectar_db()
        session.delete(venda)
        session.commit()

    @classmethod
    def update(cls, venda_antiga: Vendas, venda_nova: Vendas, session=None):
        if not session:
            session = conectar_db()
        # Atualize os atributos conforme necessário
        venda_antiga.vendedor = venda_nova.vendedor
        venda_antiga.comprador = venda_nova.comprador
        venda_antiga.quantidadevendida = venda_nova.quantidadevendida
        venda_antiga.valorvendido = venda_nova.valorvendido
        venda_antiga.data = venda_nova.data
        session.commit()

class DaoEstoque:
    @classmethod
    def save(cls, produto: Produtos, quantidade, session=None):
        if not session:
            session = conectar_db()
        estoque = Estoque(produto=produto, quantidade=quantidade)
        session.add(estoque)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Estoque).all()

    @classmethod
    def delete(cls, estoque: Estoque, session=None):
        if not session:
            session = conectar_db()
        session.delete(estoque)
        session.commit()

    @classmethod
    def update(cls, estoque_antigo: Estoque, estoque_novo: Estoque, session=None):
        if not session:
            session = conectar_db()
        estoque_antigo.produto = estoque_novo.produto
        estoque_antigo.quantidade = estoque_novo.quantidade
        session.commit()

class DaoFornecedor:
    @classmethod
    def save(cls, fornecedor: Fornecedor, session=None):
        if not session:
            session = conectar_db()
        session.add(fornecedor)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Fornecedor).all()

    @classmethod
    def delete(cls, fornecedor: Fornecedor, session=None):
        if not session:
            session = conectar_db()
        session.delete(fornecedor)
        session.commit()

    @classmethod
    def update(cls, fornecedor_antigo: Fornecedor, fornecedor_novo: Fornecedor, session=None):
        if not session:
            session = conectar_db()
        fornecedor_antigo.nome = fornecedor_novo.nome
        fornecedor_antigo.cnpj = fornecedor_novo.cnpj
        fornecedor_antigo.endereco = fornecedor_novo.endereco
        fornecedor_antigo.telefone = fornecedor_novo.telefone
        fornecedor_antigo.email = fornecedor_novo.email
        session.commit()

class DaoPessoa:
    @classmethod
    def save(cls, pessoa: Pessoa, session=None):
        if not session:
            session = conectar_db()
        session.add(pessoa)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Pessoa).all()

    @classmethod
    def delete(cls, pessoa: Pessoa, session=None):
        if not session:
            session = conectar_db()
        session.delete(pessoa)
        session.commit()

    @classmethod
    def update(cls, pessoa_antiga: Pessoa, pessoa_nova: Pessoa, session=None):
        if not session:
            session = conectar_db()
        pessoa_antiga.nome = pessoa_nova.nome
        pessoa_antiga.cpf = pessoa_nova.cpf
        pessoa_antiga.telefone = pessoa_nova.telefone
        pessoa_antiga.endereco = pessoa_nova.endereco
        pessoa_antiga.email = pessoa_nova.email
        session.commit()

class DaoCliente:
    @classmethod
    def save(cls, cliente: Cliente, session=None):
        if not session:
            session = conectar_db()
        session.add(cliente)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Cliente).all()

    @classmethod
    def delete(cls, cliente: Cliente, session=None):
        if not session:
            session = conectar_db()
        session.delete(cliente)
        session.commit()

    @classmethod
    def update(cls, cliente_antigo: Cliente, cliente_novo: Cliente, session=None):
        if not session:
            session = conectar_db()
        cliente_antigo.nome = cliente_novo.nome
        cliente_antigo.cpf = cliente_novo.cpf
        cliente_antigo.telefone = cliente_novo.telefone
        cliente_antigo.endereco = cliente_novo.endereco
        cliente_antigo.email = cliente_novo.email
        session.commit()

class DaoFuncionario:
    @classmethod
    def save(cls, funcionario: Funcionario, session=None):
        if not session:
            session = conectar_db()
        session.add(funcionario)
        session.commit()

    @classmethod
    def read(cls, session=None):
        if not session:
            session = conectar_db()
        return session.query(Funcionario).all()

    @classmethod
    def delete(cls, funcionario: Funcionario, session=None):
        if not session:
            session = conectar_db()
        session.delete(funcionario)
        session.commit()

    @classmethod
    def update(cls, funcionario_antigo: Funcionario, funcionario_novo: Funcionario, session=None):
        if not session:
            session = conectar_db()
        funcionario_antigo.idfuncionario = funcionario_novo.idfuncionario
        funcionario_antigo.cargo = funcionario_novo.cargo
        funcionario_antigo.salario = funcionario_novo.salario
        session.commit()