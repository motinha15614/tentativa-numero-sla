================
# SISTEMA DE MERCADO
# =========================

produtos = []
historico = []


# =========================
# LOGIN
# =========================

def login():
    usuario_correto = "admin"
    senha_correta = "123"

    tentativas = 0

    while tentativas < 3:

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            return True
        else:
            tentativas += 1
            print("Login incorreto.")
    print("Sistema bloqueado.")
    return False


def cadastrar_produto():

    codigo = input("Código do produto: ")

    # Verifica código repetido
    for produto in produtos:
        if produto["codigo"] == codigo:
            print("Código já cadastrado.")
            return

    nome = input("Nome do produto: ")

    preco = float(input("Preço: "))

    if preco < 0:
        print("Preço inválido.")
        return

    estoque = int(input("Estoque: "))

    if estoque < 0:
        print("Estoque inválido.")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar():

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS ===")

    for produto in produtos:

        print("-------------------")
        print("Código:", produto["codigo"])
        print("Nome:", produto["nome"])
        print("Preço: R$", produto["preco"])
        print("Estoque:", produto["estoque"])

def repor_estoque():

    codigo = input("Código do produto: ")

    for produto in produtos:

        if produto["codigo"] == codigo:

            quantidade = int(input("Quantidade para repor: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
                return

            produto["estoque"] += quantidade

            print("Estoque atualizado.")
            return

    print("Produto não encontrado.")

def venda():

    codigo = input("Digite o código do produto: ")

    for produto in produtos:

        if produto["codigo"] == codigo:

            quantidade = int(input("Quantidade: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
                return

            if quantidade > produto["estoque"]:
                print("Estoque insuficiente.")
                return

            total = quantidade * produto["preco"]

            produto["estoque"] -= quantidade
            # Histórico
            historico.append(produto["nome"])

            print("\n=== CUPOM FISCAL ===")
            print("Produto:", produto["nome"])
            print("Quantidade:", quantidade)
            print("Total: R$", total)

            return

    print("Produto não encontrado.")

def relatorio():

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    mais_caro = produtos[0]
    maior_estoque = produtos[0]

    valor_total = 0
    quantidade_total = 0

    for produto in produtos:

        if produto["preco"] > mais_caro["preco"]:
            mais_caro = produto

        if produto["estoque"] > maior_estoque["estoque"]:
            maior_estoque = produto

        valor_total += produto["preco"] * produto["estoque"]
        quantidade_total += produto["estoque"]

    print("\n=== RELATÓRIO ===")

    print("Produto mais caro e:", mais_caro["nome"])
    print("Produto com maior estoque e:", maior_estoque["nome"])
    print("Valor total do estoque e: R$", valor_total)
    print("Quantidade total de produtos e:", quantidade_total)


def historico():

    if len(historico) == 0:
        print("Nenhuma venda realizada.")
        return

    print("\n=== HISTÓRICO DE VENDAS ===")

    for item in historico:
        print(item)


if login():

    while True:

        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Realizar venda")
        print("4 - Repor estoque")
        print("5 - Histórico de vendas")
        print("6 - Relatório")
        print("7 - Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            historico()
        elif opcao == "4":
            repor_estoque()
        elif opcao == "5":
            historico()
        elif opcao == "6":
            relatorio()
        elif opcao == "7":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")
