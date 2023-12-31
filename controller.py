from models import *
from dao import *

class ControllerCategoria:
    @staticmethod
    def cadastrar_categoria(novacategoria):
        existe = False
        categorias = DaoCategoria.read()
        for categoria in categorias:
            if categoria.categoria == novacategoria:
                existe = True

        if not existe:
            nova_categoria = Categoria(categoria=novacategoria)
            DaoCategoria.save(nova_categoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já cadastrada!')

    @staticmethod
    def remover_categoria(categoria_remover):
        categorias = DaoCategoria.read()
        categoria_list = list(filter(lambda cat: cat.categoria == categoria_remover, categorias))

        if len(categoria_list) == 0:
            print('Categoria que deseja remover não existe!')
        else:
            DaoCategoria.delete(categoria_list[0])
            print('Categoria removida com sucesso!')

    @staticmethod
    def alterar_categoria(categoria_alterar, categoria_alterada):
        categorias = DaoCategoria.read()

        categoria_list1 = list(filter(lambda cat: cat.categoria == categoria_alterar, categorias))

        if len(categoria_list1) > 0:
            categoria_list2 = list(filter(lambda cat: cat.categoria == categoria_alterada, categorias))
            if len(categoria_list2) == 0:
                categoria = Categoria(categoria=categoria_alterada)
                DaoCategoria.update(categoria_list1[0], categoria)
                print('Categoria alterada com sucesso!')
            else:
                print('Categoria que deseja alterar para já existe!')
        else:
            print('Categoria que deseja alterar não existe!')

    def mostrar_categorias(self):
        categorias = DaoCategoria.read()
        if len(categorias) == 0:
            print('Não há categorias cadastradas!')
        else:
            for categoria in categorias:
                print(f'Categoria: {categoria.categoria}')

class ControllerEstoque:
    @staticmethod
    def cadastrar_produto(nome, preco, categoria, quantidade, session):
        categorias = DaoCategoria.read(session)
        
        print('Categorias cadastradas:', [cat.categoria for cat in categorias]) # Mostra as categorias cadastradas

        categoria_existente = any(cat.categoria == categoria for cat in categorias)
        produtos_existente = session.query(Produtos).filter_by(nome=nome).first()

        if not categoria_existente:
            print('Categoria não existe!')
        elif not produtos_existente:
            produto = Produtos(nome=nome, preco=preco, categoria=categoria)
            DaoEstoque.save(produto, quantidade, session)
            print('Produto cadastrado com sucesso!')
        else:
            print('Produto já cadastrado!')

    @staticmethod
    def remover_produto(nome, session):
        produtos = session.query(Estoque).filter_by(nome=nome).all()

        if not produtos:
            print('Produto não existe!')
        else:
            for prod in produtos:
                session.delete(prod)
            session.commit()
            print('Produto removido com sucesso!')

    @staticmethod
    def alterar_produto(nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade, session):
        produtos = session.query(Estoque).filter_by(nome=nome_alterar).all()
        categorias = DaoCategoria.read(session)

        categoria_existente = any(cat.categoria == nova_categoria for cat in categorias)

        if produtos:
            produtos_existente = session.query(Produtos).filter_by(nome=novo_nome).first()
            if not produtos_existente:
                if categoria_existente:
                    for prod in produtos:
                        prod.produto.nome = novo_nome
                        prod.produto.preco = novo_preco
                        prod.produto.categoria = nova_categoria
                        prod.quantidade = nova_quantidade
                    session.commit()
                    print('Produto alterado com sucesso!')
                else:
                    print('A nova categoria não existe!')
            else:
                print('Já existe um produto com o novo nome!')
        else:
            print('Produto que deseja alterar não existe!')

    def mostrar_produtos(self, session):
        produtos = DaoEstoque.read(session)
        if not produtos:
            print('Não há produtos cadastrados!')
        else:
            for prod in produtos:
                print(f'Produto: {prod.produto.nome}, Preço: {prod.produto.preco}, Categoria: {prod.produto.categoria}, Quantidade: {prod.quantidade}')

class ControllerVendas:
    @staticmethod
    def cadastrar_venda(itensvendidos, vendedor, comprador, quantidadevendida, session, data=None):
        if data is None:
            data = datetime.now().strftime("%d/%m/%Y")

        produtos_estoque = session.query(Estoque).filter_by(nome=itensvendidos.nome).first()

        if produtos_estoque:
            if produtos_estoque.quantidade >= quantidadevendida:
                valorvendido = float(itensvendidos.preco) * quantidadevendida

                venda = Vendas(itensvendidos=itensvendidos, vendedor=vendedor, comprador=comprador, quantidadevendida=quantidadevendida, valorvendido=valorvendido, data=data)
                DaoVendas.save(venda, session)

                # Atualiza a quantidade no estoque
                novo_quantidade = produtos_estoque.quantidade - quantidadevendida
                produtos_estoque.quantidade = novo_quantidade
                session.commit()

                print(f'Venda cadastrada com sucesso!')
            else:
                print(f'Quantidade insuficiente em estoque para o produto "{itensvendidos.nome}".')
        else:
            print(f'O produto "{itensvendidos.nome}" não está disponível em estoque.')

    def mostrar_vendas(self, session):
        vendas = DaoVendas.read(session)
        if not vendas:
            print('Não há vendas cadastradas!')
        else:
            for v in vendas:
                print(f'Item: {v.itensvendidos.nome}, Vendedor: {v.vendedor}, Comprador: {v.comprador}, Quantidade: {v.quantidadevendida}, Valor: {v.valorvendido}, Data: {v.data}')

class ControllerCliente:
    @staticmethod
    def cadastrar_cliente(nome, cpf, telefone, endereco, email, idcliente, session):
        clientes = DaoCliente.read(session)
        
        # Verifica se o cliente já existe com base no ID
        clientes_existentes = list(filter(lambda cli: cli.idcliente == idcliente, clientes))

        if len(clientes_existentes) == 0:
            # Se não existir, cadastra o cliente
            cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, email=email, idcliente=idcliente)
            DaoCliente.save(cliente, session)
            print('Cliente cadastrado com sucesso!')
        else:
            print('Cliente com ID já cadastrado!')

    @staticmethod
    def remover_cliente(cpf, session):
        clientes = DaoCliente.read(session)
        
        # Verifica se o cliente já existe com base no CPF
        clientes_existentes = list(filter(lambda cli: cli.cpf == cpf, clientes))

        if len(clientes_existentes) > 0:
            # Remove o cliente
            for cli in clientes_existentes:
                session.delete(cli)
            session.commit()
            print('Cliente removido com sucesso!')
        else:
            print('Cliente não encontrado!')

    @staticmethod
    def alterar_cliente(cpf_alterar, nome, cpf, telefone, endereco, email, idcliente, session):
        clientes = DaoCliente.read(session)

        cliente_list = list(filter(lambda cli: cli.cpf == cpf_alterar, clientes))

        if len(cliente_list) > 0:
            # Atualiza os dados do cliente
            for cli in cliente_list:
                cli.nome = nome
                cli.cpf = cpf
                cli.telefone = telefone
                cli.endereco = endereco
                cli.email = email
                cli.idcliente = idcliente

            session.commit()
            print('Cliente alterado com sucesso!')
        else:
            print('Cliente não encontrado!')
    
    def mostrar_clientes(self, session):
        clientes = DaoCliente.read(session)

        if not clientes:
            print('Cliente não encontrado!')
        else:
            for cli in clientes:
                print(f'Nome: {cli.nome}, CPF: {cli.cpf}, Telefone: {cli.telefone}, Endereço: {cli.endereco}, Email: {cli.email}, ID: {cli.idcliente}')

class ControllerFornecedor:
    @staticmethod
    def cadastrar_fornecedor(nome, cnpj, endereco, telefone, email, session):
        fornecedores = DaoFornecedor.read(session)
        
        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj, fornecedores))

        if len(fornecedores_existentes) == 0:
            # Se não existir, cadastra o forncecedor
            fornecedor = Fornecedor(nome=nome, cnpj=cnpj, endereco=endereco, telefone=telefone, email=email)
            DaoFornecedor.save(fornecedor, session)
            print('Fornecedor cadastrado com sucesso!')
        else:
            print('Fornecedor com CNPJ já cadastrado!')

    @staticmethod
    def remover_fornecedor(cnpj, session):
        fornecedores = DaoFornecedor.read(session)
        
        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj, fornecedores))

        if len(fornecedores_existentes) > 0:
            # Remove o forncedor
            for forn in fornecedores_existentes:
                session.delete(forn)
            session.commit()
            print('Fornecedor removido com sucesso!')
        else:
            print('Fornecedor não encontrado!')

    @staticmethod
    def alterar_fornecedor(cnpj_alterar, nome, cnpj, endereco, telefone, email, session):
        fornecedores = DaoFornecedor.read(session)

        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj_alterar, fornecedores))

        if len(fornecedores_existentes) > 0:
            # Atualiza os dados do Fornecedor
            for forn in fornecedores_existentes:
                forn.nome = nome
                forn.cnpj = cnpj
                forn.endereco = endereco
                forn.telefone = telefone
                forn.email = email

            session.commit()
            print('Fornecedor alterado com sucesso!')
        else:
            print('Fornecedor não encontrado!')
    
    def mostrar_fornecedor(self, session):
        fornecedores = DaoFornecedor.read(session)

        if len(fornecedores) == 0:
            print('Fornecedor não encontrado!')
        else:
            for forn in fornecedores:
                print(f'Nome: {forn.nome}, CNPJ: {forn.cnpj}, Endereço: {forn.endereco}, Telefone: {forn.telefone}, Email: {forn.email}')

class ControllerFuncionario:
    @staticmethod
    def cadastrar_funcionario(nome, cpf, telefone, endereco, email, idfuncionario, cargo, salario, session):
        funcionarios = DaoFuncionario.read(session)
        
        # Verifica se o funcionario já existe com base idfuncionario
        idfuncionario_existentes = list(filter(lambda idf: idf.idfuncionario == idfuncionario, funcionarios))

        if len(idfuncionario_existentes) == 0:
            # Se não existir, cadastra o funcionario
            funcionario = Funcionario(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, email=email, idfuncionario=idfuncionario, cargo=cargo, salario=salario)
            DaoFuncionario.save(funcionario, session)
            print('Funcionario cadastrado com sucesso!')
        else:
            print('Funcionario com idfuncionario já cadastrado!')

    @staticmethod
    def remover_funcionario(idfuncionario, session):
        funcionarios = DaoFuncionario.read(session)
        
        # Verifica se o funcionario já existe com base idfuncionario
        funcionarios_existentes = list(filter(lambda func: func.idfuncionario == idfuncionario, funcionarios))

        if len(funcionarios_existentes) > 0:
            # Remove o funcionario
            for func in funcionarios_existentes:
                session.delete(func)
            session.commit()
            print('Funcionário removido com sucesso!')
        else:
            print('Funcionário não encontrado!')

    @staticmethod
    def alterar_funcionario(idfuncionario_alterar, nome, cpf, endereco, telefone, email, idfuncionario, cargo, salario, session):
        funcionario = DaoFuncionario.read(session)

        funcionarios_existentes = list(filter(lambda func: func.idfuncionario == idfuncionario_alterar, funcionario))

        if len(funcionarios_existentes) > 0:
            # Atualiza os dados do Fornecedor
            for func in funcionarios_existentes:
                func.nome = nome
                func.cpf = cpf
                func.endereco = endereco
                func.telefone = telefone
                func.email = email
                func.idfuncionario = idfuncionario
                func.cargo = cargo
                func.salario = salario

            session.commit()
            print('Funcionario alterado com sucesso!')
        else:
            print('Funcionario não encontrado!')
    
    def mostrar_funcionario(self, session):
        funcionario = DaoFuncionario.read(session)

        if len(funcionario) == 0:
            print('Funcionario não encontrado!')
        else:
            for func in funcionario:
                print(f'Nome: {func.nome}, CPF: {func.cpf}, Endereço: {func.endereco}, Telefone: {func.telefone}, Email: {func.email}, ID: {func.idfuncionario}, Cargo: {func.cargo}, Salário: {func.salario}')


################################################# ALTERADO #################################################################


# a = ControlerCategoria()
# a.cadastrar_categoria('Frutas')
# a.remover_categoria('Frutas')
# a.alterar_categoria('Verduras', 'Carnes')
# a.mostrar_categorias()

# a = ControlerEstoque()
# a.cadastrar_produto('Maca', 2.50, 'Frutas', 10)
# a.remover_produto('banana')
# a.alterar_produto('Maca', 'Banana', 5.50, 'Frutas', 1)
# a.mostrar_produtos()

# a = ControlerVendas()
# a.cadastrar_venda(Produtos('Banana', 5.50, 'Frutas'), 'Joao', 'Maria', 2)
# a.mostrar_vendas()

# a = ControlerCliente()
# a.cadastrar_cliente('Joao', '123', '123', '123', '123', '123')
# a.remover_cliente('123')
# a.alterar_cliente('123', 'Maria', '321', '123', '123', '123', '123')
# a.mostrar_clientes()

# a = ControlerFornecedor()
# a.cadastrar_fornecedor('Joao', '123', '123', 'teste@teste.com', '123')
# a.remover_fornecedor('123')
# a.alterar_fornecedor('123', 'Maria', '123', '123', '123', '123')
# a.mostrar_fornecedor()

# a = ControlerFuncionario()
# a.cadastrar_funcionario('Joao', '123', 'rua teste', '123', 'teste@teste.com', '123', 'teste', '123')
# a.remover_funcionario('123')
# a.alterar_funcionario('123', 'Maria', '321', 'rua teste', '321', 'teste@teste.com', '321', 'teste', '321')
# a.mostrar_funcionario()