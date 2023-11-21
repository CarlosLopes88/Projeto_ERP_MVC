#View

import controler
import os.path

def criar_arquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as file:
                file.write('')

criar_arquivos('categorias.txt', 'estoque.txt',
                 'fornecedores.txt', 'pessoas.txt',
                 'funcionarios.txt', 'clientes.txt', 'vendas.txt')

print("Bem-vindo ao nosso ERP!")

if __name__ == "__main__":
    while True:
        try:
            local = int(input("Digite 1 para acessar o menu de categorias \n"
                              "Digite 2 para acessar o menu de estoque \n"
                              "Digite 3 para acessar o menu de fornecedores \n"
                              "Digite 4 para acessar o menu de pessoas \n"
                              "Digite 5 para acessar o menu de funcionarios \n"
                              "Digite 6 para acessar o menu de clientes \n"
                              "Digite 7 para acessar o menu de vendas \n"
                              "Digite 0 para sair \n"))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if local == 1:
            categoria = controler.ControlerCategoria()
            while True: 
                opcao = int(input("Digite 1 para cadastrar um categoria \n"
                          "Digite 2 para remover um categoria \n"
                          "Digite 3 para alterar um categoria \n"
                          "Digite 4 mostrar categoria \n"
                          "Digite 0 para sair \n"))
                
                if opcao == 1:
                    input_usuario = input("Digite o nome da categoria: ")
                    print(input_usuario)
                    categoria.cadastrar_categoria(input_usuario)
                elif opcao == 2:
                    input_usuario = input("Digite o nome da categoria: ")
                    categoria.remover_categoria(input_usuario)
                elif opcao == 3:
                    input_usuario_1 = input("Digite o nome da categoria: ")
                    input_usuario_2 = input("Digite o novo nome da categoria: ")
                    categoria.alterar_categoria(input_usuario_1, input_usuario_2)
                elif opcao == 4:
                    categoria.mostrar_categorias()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")
        
        elif local == 2:
            estoque = controler.ControlerEstoque()
            while True:
                opcao = int(input("Digite 1 para cadastrar um produto\n"
                                  "Digite 2 para remover um produto\n"
                                  "Digite 3 para alterar um produto\n"
                                  "Digite 4 para mostrar produtos\n"
                                  "Digite 0 para sair\n"))

                if opcao == 1:
                    nome = input("Digite o nome do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = int(input("Digite a quantidade do produto: "))
                    estoque.cadastrar_produto(nome, preco, categoria, quantidade)
                elif opcao == 2:
                    nome = input("Digite o nome do produto a ser removido: ")
                    estoque.remover_produto(nome)
                elif opcao == 3:
                    nome_alterar = input("Digite o nome do produto a ser alterado: ")
                    novo_nome = input("Digite o novo nome do produto: ")
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    nova_categoria = input("Digite a nova categoria do produto: ")
                    nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                    estoque.alterar_produto(nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade)
                elif opcao == 4:
                    estoque.mostrar_produtos()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 3:
            fornecedores = controler.ControlerFornecedor()
            while True:
                opcao = int(input("Digite 1 para cadastrar um fornecedor\n"
                                  "Digite 2 para remover um fornecedor\n"
                                  "Digite 3 para alterar um fornecedor\n"
                                  "Digite 4 para mostrar fornecedores\n"
                                  "Digite 0 para sair\n"))

                if opcao == 1:
                    nome = input("Digite o nome do fornecedor: ")
                    cnpj = input("Digite o CNPJ do fornecedor: ")
                    endereco = input("Digite o endereço do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    email = input("Digite o email do fornecedor: ")
                    fornecedores.cadastrar_fornecedor(nome, cnpj, endereco, telefone, email)
                elif opcao == 2:
                    cnpj = input("Digite o CNPJ do fornecedor a ser removido: ")
                    fornecedores.remover_fornecedor(cnpj)
                elif opcao == 3:
                    cnpj_alterar = input("Digite o CNPJ do fornecedor a ser alterado: ")
                    nome = input("Digite o novo nome do fornecedor: ")
                    cnpj = input("Digite o novo CNPJ do fornecedor: ")
                    endereco = input("Digite o novo endereço do fornecedor: ")
                    telefone = input("Digite o novo telefone do fornecedor: ")
                    email = input("Digite o novo email do fornecedor: ")
                    fornecedores.alterar_fornecedor(cnpj_alterar, nome, cnpj, endereco, telefone, email)
                elif opcao == 4:
                    fornecedores.mostrar_fornecedor()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 4:
            pessoas = controler.ControlerPessoa()
            while True:
                opcao = int(input("Digite 1 para cadastrar uma pessoa\n"
                                "Digite 2 para remover uma pessoa\n"
                                "Digite 3 para alterar uma pessoa\n"
                                "Digite 4 para mostrar pessoas\n"
                                "Digite 0 para sair\n"))

                if opcao == 1:
                    nome = input("Digite o nome da pessoa: ")
                    cpf = input("Digite o CPF da pessoa: ")
                    telefone = input("Digite o telefone da pessoa: ")
                    endereco = input("Digite o endereço da pessoa: ")
                    email = input("Digite o email da pessoa: ")
                    idpessoa = input("Digite o ID da pessoa: ")
                    pessoas.cadastrar_pessoa(nome, cpf, telefone, endereco, email, idpessoa)
                elif opcao == 2:
                    cpf = input("Digite o CPF da pessoa a ser removida: ")
                    pessoas.remover_pessoa(cpf)
                elif opcao == 3:
                    cpf_alterar = input("Digite o CPF da pessoa a ser alterada: ")
                    nome = input("Digite o novo nome da pessoa: ")
                    cpf = input("Digite o novo CPF da pessoa: ")
                    telefone = input("Digite o novo telefone da pessoa: ")
                    endereco = input("Digite o novo endereço da pessoa: ")
                    email = input("Digite o novo email da pessoa: ")
                    idpessoa = input("Digite o novo ID da pessoa: ")
                    pessoas.alterar_pessoa(cpf_alterar, nome, cpf, telefone, endereco, email, idpessoa)
                elif opcao == 4:
                    pessoas.mostrar_pessoas()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 5:
            funcionarios = controler.ControlerFuncionario()
            while True:
                opcao = int(input("Digite 1 para cadastrar um funcionário\n"
                                "Digite 2 para remover um funcionário\n"
                                "Digite 3 para alterar um funcionário\n"
                                "Digite 4 para mostrar funcionários\n"
                                "Digite 0 para sair\n"))

                if opcao == 1:
                    nome = input("Digite o nome do funcionário: ")
                    cpf = input("Digite o CPF do funcionário: ")
                    telefone = input("Digite o telefone do funcionário: ")
                    endereco = input("Digite o endereço do funcionário: ")
                    email = input("Digite o email do funcionário: ")
                    idfuncionario = input("Digite o ID do funcionário: ")
                    cargo = input("Digite o cargo do funcionário: ")
                    salario = input("Digite o salário do funcionário: ")
                    funcionarios.cadastrar_funcionario(nome, cpf, telefone, endereco, email, idfuncionario, cargo, salario)
                elif opcao == 2:
                    idfuncionario = input("Digite o ID do funcionário a ser removido: ")
                    funcionarios.remover_funcionario(idfuncionario)
                elif opcao == 3:
                    idfuncionario_alterar = input("Digite o ID do funcionário a ser alterado: ")
                    nome = input("Digite o novo nome do funcionário: ")
                    cpf = input("Digite o novo CPF do funcionário: ")
                    telefone = input("Digite o novo telefone do funcionário: ")
                    endereco = input("Digite o novo endereço do funcionário: ")
                    email = input("Digite o novo email do funcionário: ")
                    idfuncionario = input("Digite o novo ID do funcionário: ")
                    cargo = input("Digite o novo cargo do funcionário: ")
                    salario = input("Digite o novo salário do funcionário: ")
                    funcionarios.alterar_funcionario(idfuncionario_alterar, nome, cpf, endereco, telefone, email, idfuncionario, cargo, salario)
                elif opcao == 4:
                    funcionarios.mostrar_funcionario()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 6:
            clientes = controler.ControlerCliente()
            while True:
                opcao = int(input("Digite 1 para cadastrar um cliente\n"
                                  "Digite 2 para remover um cliente\n"
                                  "Digite 3 para alterar um cliente\n"
                                  "Digite 4 para mostrar clientes\n"
                                  "Digite 0 para sair\n"))

                if opcao == 1:
                    nome = input("Digite o nome do cliente: ")
                    cpf = input("Digite o CPF do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    email = input("Digite o email do cliente: ")
                    idcliente = input("Digite o ID do cliente: ")
                    clientes.cadastrar_cliente(nome, cpf, telefone, endereco, email, idcliente)
                elif opcao == 2:
                    cpf = input("Digite o CPF do cliente a ser removido: ")
                    clientes.remover_cliente(cpf)
                elif opcao == 3:
                    cpf_alterar = input("Digite o CPF do cliente a ser alterado: ")
                    nome = input("Digite o novo nome do cliente: ")
                    cpf = input("Digite o novo CPF do cliente: ")
                    telefone = input("Digite o novo telefone do cliente: ")
                    endereco = input("Digite o novo endereço do cliente: ")
                    email = input("Digite o novo email do cliente: ")
                    idcliente = input("Digite o novo ID do cliente: ")
                    clientes.alterar_cliente(cpf_alterar, nome, cpf, telefone, endereco, email, idcliente)
                elif opcao == 4:
                    clientes.mostrar_clientes()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 7:
            vendas = controler.ControlerVendas()
            while True:
                opcao = int(input("Digite 1 para cadastrar uma venda\n"
                                "Digite 2 para mostrar vendas\n"
                                "Digite 0 para sair\n"))

                if opcao == 1:
                    itens_vendidos_nome = input("Digite o nome do item vendido: ")
                    vendedor = input("Digite o nome do vendedor: ")
                    comprador = input("Digite o nome do comprador: ")
                    quantidade_vendida = int(input("Digite a quantidade vendida: "))
                    vendas.cadastrar_venda(itens_vendidos_nome, vendedor, comprador, quantidade_vendida)
                elif opcao == 2:
                    vendas.mostrar_vendas()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")

        elif local == 0:
            print("Obrigado por usar o sistema. Até mais!")
            break

        else:
            print("Opção inválida!")