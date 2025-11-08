#  Sistema Gerenciador (Python + SQL)

Este projeto é um **Sistema Gerenciador** desenvolvido em **Python**, utilizando **SQL** para armazenamento dos dados.  
A aplicação é executada diretamente no **terminal**, oferecendo um fluxo simples e eficiente para gerenciamento de **clientes**, **produtos** e **vendas**, mantendo controle automático de estoque e preços.

---

##  Funcionalidades Principais

###  Cadastro de Cliente
- Adicionar novos clientes ao banco
- Armazenamento em tabela própria para consultas futuras

###  Cadastro de Produto
- Inserção de novos produtos com nome, código, preço e quantidade em estoque
- Dados salvos no banco de dados para controle contínuo

###  Registro de Venda
- Registrar vendas vinculando **cliente** e **produto**
- Cálculo automático da quantidade vendida e valor total da transação

###  Atualização de Estoque
- Redução automática do estoque ao efetuar uma venda
- Evita vendas acima da quantidade disponível

###  Atualização de Preço
- Possibilidade de alterar preços de produtos já cadastrados
- Mantém os valores sempre atualizados

---

##  Tecnologias Utilizadas

| Tecnologia | Uso |
|----------|------|
| **Python 3** | Aplicação e lógica de execução |
| **  SQLite ** | Armazenamento e gerenciamento de dados |
| **Terminal / Console** | Interface de interação com o usuário |

---

##  Como Executar

1. Certifique-se de ter **Python 3** instalado.
2. Configure o banco de dados caso necessário (ou utilize o já fornecido).
3. Execute o programa principal no terminal:

## Contribuição

Sinta-se livre para sugerir melhorias, relatar bugs ou adaptar este sistema às suas necessidades!