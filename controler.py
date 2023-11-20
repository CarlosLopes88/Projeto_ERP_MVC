#controller

from models import *
from dao import *
from datetime import datetime

class ControlerCategoria:
    @staticmethod
    def cadastrar_categoria(novacategoria):
        existe = False
        categorias = DaoCategoria.read()
        for i in categorias:
            if i.categoria == novacategoria:
                existe = True

        if not existe:
            DaoCategoria.save(novacategoria)
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
            categorias = [cat for cat in categorias if cat.categoria != categoria_remover]
            print('Categoria removida com sucesso!')

            with open('categorias.txt', 'w') as file:
                for cat in categorias:
                    file.write(f'{cat.categoria}\n')

    @staticmethod
    def alterar_categoria(categoria_alterar, categoria_alterada):
        categorias = DaoCategoria.read()

        categoria_list1 = list(filter(lambda cat: cat.categoria == categoria_alterar, categorias))

        if len(categoria_list1) > 0:
            categoria_list2 = list(filter(lambda cat: cat.categoria == categoria_alterada, categorias))
            if len(categoria_list2) == 0:
                categorias = [Categoria(categoria_alterada) if cat.categoria == categoria_alterar else cat for cat in categorias]
                print('Categoria alterada com sucesso!')
            else:
                print('Categoria que deseja alterar para já existe!')
        else:
            print('Categoria que deseja alterar não existe!')

        with open('categorias.txt', 'w') as file:
            for cat in categorias:
                file.write(f'{cat.categoria}\n')

    def mostrar_categorias(self):
        categoria = DaoCategoria.read()
        if len(categoria) == 0:
            print('Não há a categoria cadastradas!')
        else:
            for i in categoria:
                print(f'Categoria: {i.categoria}')

class ControlerEstoque:
    @staticmethod
    def cadastrar_produto(nome, preco, categoria, quantidade):
        estoque = DaoEstoque.read()
        categorias = DaoCategoria.read()

        print('Categorias cadastradas:', [cat.categoria for cat in categorias]) # Mostra as categorias cadastradas

        categorias_encontradas = list(filter(lambda cat: cat.categoria == categoria, categorias))
        produtos_existente = list(filter(lambda prod: prod.produto.nome == nome, estoque))

        if len(categorias_encontradas) == 0:
            print('Categoria não existe!')
        else:
            if len(produtos_existente) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.save(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já cadastrado!')

    @staticmethod
    def remover_produto(self, nome):
        estoque = DaoEstoque.read()
        produtos = list(filter(lambda prod: prod.produto.nome == nome, estoque))

        if len(produtos) == 0:
            print('Produto não existe!')
        else:
            estoque = [prod for prod in estoque if prod.produto.nome != nome]
            print('Produto removido com sucesso!')

            with open('estoque.txt', 'w') as file:
                for prod in estoque:
                    file.write(f'{prod.produto.nome}|{prod.produto.preco}|{prod.produto.categoria}|{prod.quantidade}\n')

    @staticmethod
    def alterar_produto(nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        estoque = DaoEstoque.read()
        categorias = DaoCategoria.read()

        categoria_existente = any(cat.categoria == nova_categoria for cat in categorias)

        produtos_list1 = list(filter(lambda prod: prod.produto.nome == nome_alterar, estoque))

        if len(produtos_list1) > 0:
            produtos_list2 = list(filter(lambda prod: prod.produto.nome == novo_nome, estoque))
            if len(produtos_list2) == 0:
                if categoria_existente:
                    estoque = [Estoque(Produtos(novo_nome, novo_preco, nova_categoria), nova_quantidade) if prod.produto.nome == nome_alterar else prod for prod in estoque]
                    print('Produto alterado com sucesso!')
                else:
                    print('A nova categoria não existe!')
            else:
                print('Já existe um produto com o novo nome!')
        else:
            print('Produto que deseja alterar não existe!')

        with open('estoque.txt', 'w') as file:
            for prod in estoque:
                file.write(f'{prod.produto.nome}|{prod.produto.preco}|{prod.produto.categoria}|{prod.quantidade}\n')

    def mostrar_produtos(self):
        estoque = DaoEstoque.read()
        if len(estoque) == 0:
            print('Não há produtos cadastrados!')
        else:
            for prod in estoque:
                print(f'Produto: {prod.produto.nome}, Preço: {prod.produto.preco}, Categoria: {prod.produto.categoria}, Quantidade: {prod.quantidade}')

class ControlerVendas:
    @staticmethod
    def cadastrar_venda(itensvendidos, vendedor, comprador, quantidadevendida, data=None):
        if data is None:
            data = datetime.now().strftime("%d/%m/%Y")

        estoque = DaoEstoque.read()
        produtos_estoque = list(filter(lambda prod: prod.produto.nome == itensvendidos.nome, estoque))

        if len(produtos_estoque) == 0:
            print(f'O produto "{itensvendidos.nome}" não está disponível em estoque.')
        else:
            estoque_produto = produtos_estoque[0]
            if int(estoque_produto.quantidade) >= quantidadevendida:
                valorvendido = float(itensvendidos.preco) * quantidadevendida

                venda = Vendas(itensvendidos, vendedor, comprador, quantidadevendida, valorvendido, data)
                DaoVendas.save(venda)

                # Atualiza a quantidade no arquivo de estoque
                novo_quantidade = int(estoque_produto.quantidade) - quantidadevendida
                estoque_produto.quantidade = str(novo_quantidade)
                with open('estoque.txt', 'w') as file:
                    for prod in estoque:
                        file.write(f'{prod.produto.nome}|{prod.produto.preco}|{prod.produto.categoria}|{prod.quantidade}\n')

                print(f'Venda cadastrada com sucesso!')
            else:
                print(f'Quantidade insuficiente em estoque para o produto "{itensvendidos.nome}".')

    def mostrar_vendas(self):
        vendas = DaoVendas.read()
        if len(vendas) == 0:
            print('Não há vendas cadastradas!')
        else:
            for v in vendas:
                print(f'Item: {v.itensvendidos.nome}, Vendedor: {v.vendedor}, Comprador: {v.comprador}, Quantidade: {v.quantidadevendida}, Valor: {v.valorvendido}, Data: {v.data}')

class ControlerCliente:
    @staticmethod
    def cadastrar_cliente(nome, cpf, telefone, endereco, email, idcliente):
        clientes = DaoCliente.read()
        
        # Verifica se o cliente já existe com base no ID
        clientes_existentes = list(filter(lambda cli: cli.idcliente == idcliente, clientes))

        if len(clientes_existentes) == 0:
            # Se não existir, cadastra o cliente
            cliente = Cliente(nome, cpf, telefone, endereco, email, idcliente)
            DaoCliente.save(cliente)
            print('Cliente cadastrado com sucesso!')
        else:
            print('Cliente com ID já cadastrado!')

    @staticmethod
    def remover_cliente(cpf):
        clientes = DaoCliente.read()
        
        # Verifica se o cliente já existe com base no CPF
        clientes_existentes = list(filter(lambda cli: cli.cpf == cpf, clientes))

        if len(clientes_existentes) > 0:
            # Remove o cliente
            clientes = [cli for cli in clientes if cli.cpf != cpf]

            # Atualiza a lista no arquivo clientes.txt
            with open('clientes.txt', 'w') as file:
                for cli in clientes:
                    file.write(f'{cli.nome}|{cli.cpf}|{cli.telefone}|{cli.endereco}|{cli.email}|{cli.idcliente}\n')

            print('Cliente removido com sucesso!')
        else:
            print('Cliente não encontrado!')

    @staticmethod
    def alterar_cliente(cpf_alterar, nome, cpf, telefone, endereco, email, idcliente):
        clientes = DaoCliente.read()

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

            # Atualiza a lista no arquivo clientes.txt
            with open('clientes.txt', 'w') as file:
                file.writelines([f'{cli.nome}|{cli.cpf}|{cli.telefone}|{cli.endereco}|{cli.email}|{cli.idcliente}\n' for cli in clientes])

            print('Cliente alterado com sucesso!')
        else:
            print('Cliente não encontrado!')
    
    def mostrar_clientes(self):
        clientes = DaoCliente.read()

        if len(clientes) == 0:
            print('Cliente não encontrado!')
        else:
            for cli in clientes:
                print(f'Nome: {cli.nome}, CPF: {cli.cpf}, Telefone: {cli.telefone}, Endereço: {cli.endereco}, Email: {cli.email}, ID: {cli.idcliente}')

class ControlerFornecedor:
    @staticmethod
    def cadastrar_fornecedor(nome, cnpj, endereco, telefone, email):
        fornecedores = DaoFornecedor.read()
        
        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj, fornecedores))

        if len(fornecedores_existentes) == 0:
            # Se não existir, cadastra o forncecedor
            fornecedor = Fornecedor(nome, cnpj, endereco, telefone, email)
            DaoFornecedor.save(fornecedor)
            print('Fornecedor cadastrado com sucesso!')
        else:
            print('Fornecedor com CNPJ já cadastrado!')

    @staticmethod
    def remover_fornecedor(cnpj):
        fornecedores = DaoFornecedor.read()
        
        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj, fornecedores))

        if len(fornecedores_existentes) > 0:
            # Remove o forncedor
            fornecedores = [forn for forn in fornecedores if forn.cnpj != cnpj]

            # Atualiza a lista no arquivo clientes.txt
            with open('fornecedores.txt', 'w') as file:
                for forn in fornecedores:
                    file.write(f'{forn.nome}|{forn.cnpj}|{forn.endereco}|{forn.telefone}|{forn.email}\n')
            print('Cliente removido com sucesso!')
        else:
            print('Cliente não encontrado!')

    @staticmethod
    def alterar_fornecedor(cnpj_alterar, nome, cnpj, endereco, telefone, email):
        fornecedores = DaoFornecedor.read()

        # Verifica se o forncedor já existe com base no CNPJ
        fornecedores_existentes = list(filter(lambda forn: forn.cnpj == cnpj, fornecedores))

        if len(fornecedores_existentes) > 0:
            # Atualiza os dados do Fornecedor
            for forn in fornecedores_existentes:
                forn.nome = nome
                forn.cnpj = cnpj
                forn.endereco = endereco
                forn.telefone = telefone
                forn.email = email

            # Atualiza a lista no arquivo forncedores.txt
            with open('fornecedores.txt', 'w') as file:
                file.writelines([f'{forn.nome}|{forn.cnpj}|{forn.endereco}|{forn.telefone}|{forn.email}|\n' for forn in fornecedores])

            print('Fornecedor alterado com sucesso!')
        else:
            print('Fornecedor não encontrado!')
    
    def mostrar_fornecedor(self):
        fornecedores = DaoFornecedor.read()

        if len(fornecedores) == 0:
            print('Fornecedor não encontrado!')
        else:
            for forn in fornecedores:
                print(f'Nome: {forn.nome}, CNPJ: {forn.cnpj}, Endereço: {forn.endereco}, Telefone: {forn.telefone}, Email: {forn.email}')

class ControlerFuncionario:
    @staticmethod
    def cadastrar_funcionario(nome, cpf, telefone, endereco, email, idfuncionario, cargo, salario):
        funcionarios = DaoFuncionario.read()
        
        # Verifica se o funcionario já existe com base idfuncionario
        idfuncionario_existentes = list(filter(lambda idf: idf.idfuncionario == idfuncionario, funcionarios))

        if len(idfuncionario_existentes) == 0:
            # Se não existir, cadastra o funcionario
            funcionario = Funcionario(nome, cpf, telefone, endereco, email, idfuncionario, cargo, salario)
            DaoFuncionario.save(funcionario)
            print('Funcionario cadastrado com sucesso!')
        else:
            print('Funcionario com idfuncionario já cadastrado!')

    @staticmethod
    def remover_funcionario(idfuncionario):
        funcionarios = DaoFuncionario.read()
        
        # Verifica se o funcionario já existe com base idfuncionario
        funcionarios_existentes = list(filter(lambda func: func.idfuncionario == idfuncionario, funcionarios))

        if len(funcionarios_existentes) > 0:
            # Remove o funcionario
            funcionarios = [func for func in funcionarios if func.idfuncionario != idfuncionario]

            # Atualiza a lista no arquivo funcionarios.txt
            with open('funcionarios.txt', 'w') as file:
                for func in funcionarios:
                    file.write(f'{func.nome}|{func.cpf}|{func.telefone}|{func.endereco}|{func.email}|{func.idfuncionario}|{func.cargo}|{func.salario}\n')
            print('Funcionário removido com sucesso!')
        else:
            print('Funcionário não encontrado!')

    @staticmethod
    def alterar_funcionario(idfuncionario_alterar, nome, cpf, endereco, telefone, email, idfuncionario, cargo, salario):
        funcionario = DaoFuncionario.read()

        # Verifica se o funcionario já existe com base idfuncionario
        funcionarios_existentes = list(filter(lambda func: func.idfuncionario == idfuncionario_alterar, funcionario))

        if len(funcionarios_existentes) > 0:
            # Atualiza os dados do Fornecedor
            for func in funcionarios_existentes:
                func.nome = nome
                func.cnpj = cpf
                func.endereco = endereco
                func.telefone = telefone
                func.email = email
                func.idfuncionario = idfuncionario
                func.cargo = cargo
                func.salario = salario

            # Atualiza a lista no arquivo forncedores.txt
            with open('funcionarios.txt', 'w') as file:
                file.writelines([f'{func.nome}|{func.cpf}|{func.endereco}|{func.telefone}|{func.email}|{func.idfuncionario}|{func.cargo}|{func.salario}|\n' for func in funcionario])

            print('Funcionario alterado com sucesso!')
        else:
            print('Funcionario não encontrado!')
    
    def mostrar_funcionario(self):
        funcionario = DaoFuncionario.read()

        if len(funcionario) == 0:
            print('Funcionario não encontrado!')
        else:
            for func in funcionario:
                print(f'Nome: {func.nome}, CNPJ: {func.cpf}, Endereço: {func.endereco}, Telefone: {func.telefone}, Email: {func.email}, ID: {func.idfuncionario}, Cargo: {func.cargo}, Salário: {func.salario}')

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