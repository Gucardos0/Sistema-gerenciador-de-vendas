import sqlite3


def criarTabelas():
    conexao = sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            estoque INTEGER DEFAULT 0,
            preco REAL NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id),
            FOREIGN KEY (id_produto) REFERENCES produto(id)
        );
    """)

    conexao.commit()
    conexao.close()
    print(" Tabelas criadas/verificadas com sucesso!")

def cadastrarProduto(nome, estoque, preco):
    conexao = sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produto (nome, estoque, preco) VALUES (?, ?, ?)",
        (nome, estoque, preco)
    )
    conexao.commit()
    conexao.close()
    print(" Produto cadastrado com sucesso!")



def cadastrarCliente(nome, email, telefone):
    conexao =sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone)
    )
    conexao.commit()
    conexao.close()
    print(" Cliente cadastrado com sucesso!")


def registrarVenda(id_cliente, id_produto, quantidade):

    conexao =sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()

    cursor.execute("SELECT estoque FROM produto WHERE id = ?", (id_produto,))  #procura na tabela produto o id que é passado e verifica o estoque
    estoque = cursor.fetchone() #pega a linha do que foi solicitado acima

    if estoque is None:
         print(" Produto não encontrado.") 
         
    elif estoque[0] < quantidade: # posição 0 para buscar o primiro item do "cursor.fetchone()"
        print("Estoque insuficiente")

    else:
        cursor.execute(
            " INSERT INTO venda (id_cliente, id_produto, quantidade) VALUES (?, ?, ?)",
                        (id_cliente, id_produto, quantidade))
        cursor.execute("""
            UPDATE produto SET estoque = estoque - ?
            WHERE id = ?
        """, (quantidade, id_produto))

        conexao.commit()
        print(" Venda registrada com sucesso!")
       
    

    conexao.close()
        

def atualizarEstoque(id_produto, estoque ):
    conexao =sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()
    cursor.execute(""" UPDATE produto SET estoque = ? 
                    WHERE id = ?
    
     """, (estoque,  id_produto))
    print("Produto atualizado")


    conexao.commit()
    conexao.close()


def autualizarPreco(id_produto, preco ):
    conexao =sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()
    cursor.execute(""" UPDATE produto SET preco = ? 
                    WHERE id = ?
    
     """, (preco,  id_produto))
    print("Produto atualizado")


    conexao.commit()
    conexao.close()

def listarProdutos():
    conexao =sqlite3.connect("sgv (2).db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    conexao.close()

    print(" Produtos cadastrados:")
    for p in produtos:  # p = contadora/ produto = tipo nosso array
        print(f"ID: {p[0]} | Nome: {p[1]} | Estoque: {p[2]} | Preço: R${p[3]:.2f}")



def menuPrincipal():
    criarTabelas()
    while True:
        print("\n SISTEMA DE GESTÃO DE VENDAS")
        print("1 - Cadastrar produto")
        print("2 - Cadastrar cliente")
        print("3 - Registrar venda")
        print("4 - Lista de produtos")
        print("5 - Atualizar estoque")
        print("6 - Atualizar preço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            estoque = int(input("Quantidade de estoque: "))
            preco = float(input("Preço: "))
            cadastrarProduto(nome, estoque, preco)

        elif opcao == "2":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("telefone do cliente: ")
            cadastrarCliente(nome, email, telefone)

        elif opcao == "3":
            id_cliente = int(input("ID do cliente: "))
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            registrarVenda(id_cliente, id_produto, quantidade)

        elif opcao == "4":
            listarProdutos()
        
        elif opcao == "5":
            id_produto = input("ID do produto: ")
            estoque = int(input("Estoque: "))
            atualizarEstoque(id_produto, estoque)

        elif opcao == "6":
            id_produto = input("ID do produto: ")
            preco = int(input("Preço: "))
            autualizarPreco(id_produto, preco)




        elif opcao == "0":
           break

        else:
            print("Insira um valor valido")

if __name__ == "__main__":
    menuPrincipal()