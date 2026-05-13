compra = []


# =========================
# PRODUTOS
# =========================
def escolha_filme():

    filmes = ["0 - Arroz", "1 - PS5", "2 - Abacaxi"]

    produtos = {
        "0": {"nome": "Arroz", "valor": 19.58},
        "1": {"nome": "PLAYSTATION 5", "valor": 4500},
        "2": {"nome": "Abacaxi", "valor": 19.22}
    }

    print("\n--- PRODUTOS ---")

    for filme in filmes:
        print(filme)

    escolha = input("Qual produto deseja comprar? ")

    if escolha in produtos:

        produto = produtos[escolha]

        print(f"\nProduto: {produto['nome']}")
        print(f"Valor: R$ {produto['valor']}")

        compra.append(produto["nome"])

    else:
        print("Opção inválida.")


# =========================
# PAGAMENTO
# =========================
def finalizar_pagamento():

    print("\n--- PAGAMENTO ---")

    print("\nItens da compra:")
    for item in compra:
        print("-", item)

    formas = ["1 - Débito", "2 - Crédito", "3 - Pix"]

    for item in formas:
        print(item)

    forma = input("Escolha a forma de pagamento: ")

    if forma == "1":
        print("Pagamento no débito realizado!")

    elif forma == "2":
        print("Pagamento no crédito realizado!")

    elif forma == "3":
        print("Pagamento via PIX realizado!")

    else:
        print("Forma inválida.")


# =========================
# INGRESSOS
# =========================
def calcular_ingressos():

    precos = {
        "1": {"tipo": "Inteira", "valor": 50.0},
        "2": {"tipo": "Meia-entrada", "valor": 25.0}
    }

    combo_pipoca = 20.0

    total = 0.0
    pedidos = []
    assentos_escolhidos = []

    print("\n--- SISTEMA DE INGRESSOS ---")

    while True:

        print("\n1 - Inteira")
        print("2 - Meia-entrada")
        print("0 - Finalizar")

        opcao = input("Opção: ")

        if opcao == "0":
            break

        elif opcao in precos:

            try:

                qtd = int(
                    input(
                        f"Quantos ingressos de "
                        f"{precos[opcao]['tipo']}? "
                    )
                )

                if qtd > 0:

                    for i in range(qtd):

                        assento = input(
                            f"Escolha o assento {i+1}: "
                        )

                        if assento not in assentos_escolhidos:

                            assentos_escolhidos.append(assento)

                        else:
                            print("Assento já escolhido!")

                    valor_item = (
                        precos[opcao]["valor"] * qtd
                    )

                    total += valor_item

                    texto = (
                        f"{qtd}x "
                        f"{precos[opcao]['tipo']} "
                        f"- R$ {valor_item:.2f}"
                    )

                    pedidos.append(texto)
                    compra.append(texto)

                    pipoca = input(
                        "Adicionar pipoca? (sim/não): "
                    ).lower()

                    if pipoca == "sim":

                        total += combo_pipoca

                        pedidos.append(
                            f"1x Combo Pipoca "
                            f"- R$ {combo_pipoca:.2f}"
                        )

                        compra.append("Combo Pipoca")

                        print("Pipoca adicionada!")

                else:
                    print("Quantidade inválida.")

            except ValueError:
                print("Digite um número válido.")

        else:
            print("Opção inválida.")

    # CUPOM
    cupom = input(
        "\nDigite o cupom de desconto: "
    ).upper()

    if cupom == "DESCONTO10":

        desconto = total * 0.10

        total -= desconto

        print(
            f"Desconto aplicado: "
            f"R$ {desconto:.2f}"
        )

    elif cupom != "":
        print("Cupom inválido.")

    # RESUMO
    print("\n--- RESUMO ---")

    for item in pedidos:
        print(item)

    print("\nAssentos escolhidos:")

    for assento in assentos_escolhidos:
        print("-", assento)

    print(f"\nTotal: R$ {total:.2f}")


# =========================
# USUÁRIO
# =========================
class Usuario:

    def __init__(self, nome):
        self.nome = nome


ListaUsuario = []


class Admin(Usuario):

    @staticmethod
    def adicionar():

        while True:

            add = input(
                "Deseja adicionar usuário? (s/n): "
            )

            if add == "s":

                usuario = input(
                    "Digite o nome do usuário: "
                )

                p = Usuario(usuario)

                ListaUsuario.append(p)

                print("Usuário adicionado!")

            else:
                break


# =========================
# MENU
# =========================
def menuUI():

    while True:

        print("\n====== MENU ======")
        print("1 - Comprar produto")
        print("2 - Comprar ingressos")
        print("3 - Pagamento")
        print("4 - Adicionar usuário")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            escolha_filme()

        elif escolha == "2":
            calcular_ingressos()

        elif escolha == "3":
            finalizar_pagamento()

        elif escolha == "4":
            Admin.adicionar()

        elif escolha == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


# =========================
# EXECUTAR SISTEMA
# =========================
menuUI()
