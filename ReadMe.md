## Descrição

Esse projeto tem por finalidade a criação de um ERP em python, simulando através de arquivos txt salvar informações e realizar interações via prompt de comando com o usuário.

É um sistema de gerenciamento que permite a manipulação de dados relacionados a categorias, estoque, fornecedores, pessoas, funcionários, clientes e vendas.

## Estrutura do Projeto
- **controler:** Contém os controladores para cada entidade (categoria, estoque, fornecedores, pessoas, funcionários, clientes, vendas);
- **dao:** Contém os Data Access Objects (DAO) responsáveis pela interação com o banco de dados ou arquivos de dados;
- **models:** Contém as classes de modelo para representar as entidades do sistema;
- **arquivos de dados:** Arquivos de dados iniciais (categorias.txt, estoque.txt, fornecedores.txt, pessoas.txt, funcionarios.txt, clientes.txt, vendas.txt);
- **view.py:** O arquivo principal que contém o menu e interação com o usuário do programa;
- **README.md:** Este arquivo.

Pouco a pouco vamos incrementando esse código e deixando mais robustos:

- próximos passos, revisar e incrementar as entidades;
- implementar um banco em memória em SqLite;
- alterar o arquivo dao e controller para salvar em tabelas no SqLITE.