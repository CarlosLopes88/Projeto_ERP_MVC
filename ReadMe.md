## Descrição

Esse projeto tem por finalidade a criação de uma proposta de ERP em python e realizar interações via prompt de comando com o usuário.

É um sistema de gerenciamento que permite a manipulação de dados relacionados a categorias, estoque, fornecedores, pessoas, funcionários, clientes e vendas. 

Esse projata criar tabelas via ORM em um banco local postgres e salva todas as alterações.

Esse projeto utiliza o framework Python, SQLAlchemy, Psycopg2, Docker e Postgres para o seu desenvolvimento.

## Estrutura do Projeto
- **controller:** Contém os controladores para cada entidade (categoria, estoque, fornecedores, pessoas, funcionários, clientes, vendas);
- **dao:** Contém os Data Access Objects (DAO) responsáveis pela interação com o banco de dados ou arquivos de dados;
- **models:** Contém as classes de modelo para representar as entidades do sistema;
- **view.py:** O arquivo principal que contém o menu e interação com o usuário do programa;
- **README.md:** Este arquivo.

Pouco a pouco vamos incrementando esse código e deixando mais robustos:

- próximos passos, revisar e incrementar as entidades;

## Execução do Projeto

- **Criação do banco de dados localmente:** docker run --name my_container -p 5434:5432 -e POSTGRES_USER=my_user -e POSTGRES_PASSWORD=my_user2023 -e POSTGRES_DB=my_db -d postgres:16.0 (Lembre-se de instalar o docker em sua máquina)

- **Criação do ambiente virtual:** 

    - python -m venv .venv (windows)
    - Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    - .\.venv\Scripts\activate

- **Executar os arquivos:**

    - Comando model: python view.py