from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime

USER = 'my_user'
SECRET = 'my_user2023'
HOST = 'localhost' #seria o ip do banco de dados neste caso como é local é localhost.
DATABASE = 'my_db'
PORT = '5434' #porta padrão do postgresql é 5432 mas comos estamos usando o docker, foi alterado para 5434.
CONN = f'postgresql+psycopg2://{USER}:{SECRET}@{HOST}:{PORT}/{DATABASE}' #string de conexão com o banco de dados.

engine = create_engine(CONN, echo=True) #echo=True é para mostrar o que está acontecendo no banco de dados.
session = sessionmaker(bind=engine) #criando uma sessão com o banco de dados
Base = declarative_base() #criando uma base para criar as tabelas.

class Categoria(Base):
    __tablename__ = 'categorias' #nome da tabela no banco de dados.
    id = Column(Integer, primary_key=True)
    categoria = Column(String, nullable=False)

class Produtos(Base):
    __tablename__ = 'produtos' #nome da tabela no banco de dados.
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria')

class Estoque(Base):
    __tablename__ = 'estoque' #nome da tabela no banco de dados.
    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    produto = relationship('Produtos')
    quantidade = Column(Integer, nullable=False)

class Vendas(Base):
    __tablename__ = 'vendas' #nome da tabela no banco de dados.
    id = Column(Integer, primary_key=True)
    itensvendidos_id = Column(Integer, ForeignKey('produtos.id'))
    itensvendidos = relationship('Produtos')
    vendedor = Column(String, nullable=False)
    comprador = Column(String, nullable=False)
    quantidadevendida = Column(Integer, nullable=False)
    valorvendido = Column(Integer, nullable=False)
    data = Column(DateTime, default=datetime.now)

class Fornecedor(Base):
    __tablename__ = 'fornecedores'#nome da tabela no banco de dados.
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    email = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # Adicionando uma coluna para distinguir Funcionario e Cliente
    __mapper_args__ = {'polymorphic_on': tipo}

class Funcionario(Pessoa):
    __tablename__ = 'funcionarios'
    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    idfuncionario = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    salario = Column(Integer, nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'funcionario'}

class Cliente(Pessoa):
    __tablename__ = 'clientes'
    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    idcliente = Column(String, nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'cliente'}

Base.metadata.create_all(engine) #criando as tabelas no banco de dados.