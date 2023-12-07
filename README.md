# Banco-de-dados

## Projeto de Geração de Dados para Clientes
Este projeto foi desenvolvido com o objetivo de criar três arquivos CSV contendo informações relacionadas a clientes, endereços e telefones, utilizando a biblioteca Faker.

# Funcionalidades
Geração de Dados:

Utilização da biblioteca Faker para criar conjuntos de dados fictícios de clientes, endereços e telefones.
# Persistência no Oracle:

Após a geração dos arquivos CSV, o projeto inclui a criação de tabelas, sequências e triggers no banco de dados Oracle por meio de scripts Python.
A sequência criada é utilizada para controlar a numeração automática de identificadores únicos no banco de dados.
# Inserção de Dados:

Utilização da biblioteca Pandas e Oracle DB para realizar a inserção eficiente dos dados gerados nos arquivos CSV no banco de dados Oracle.


# Pré-requisitos
Python
Bibliotecas: Faker, Pandas, OracleDB, Faker
Banco de Dados Oracle instalado e configurado
Como Utilizar
- Clone o repositório para o seu ambiente local.
- Execute os scripts Python para gerar os arquivos CSV e configurar a estrutura no banco de dados Oracle.
- Execute o script Python para inserção dos dados nos respectivos tabelas no banco de dados.
- Lembre-se de configurar as credenciais do banco de dados Oracle no script Python antes de executar as operações.

Este projeto facilita a geração e inserção de dados fictícios para testes e desenvolvimento em um ambiente Oracle.
