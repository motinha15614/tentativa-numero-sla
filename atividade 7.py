compra = []

def escolha_filme():

    filmes = ["0 - Arroz", "1 - PS5", "2 - Abacaxi"]

    produtos = {
        "0": {"nome": "Arroz", "valor": 19.58},
        "1": {"nome": "PLAYSTATION 5", "valor": 4500},
        "2": {"nome": "Abacaxi", "valor": 19.22}
    }

    print("\n--- FILMES/PRODUTOS ---")

    for filme in filmes:
        print(filme)

    escolha = input("Qual produto você gostaria de comprar? ")

    if escolha in produtos:

        produto = produtos[escolha]

        print(f"Produto: {produto['nome']}")
        print(f"Valor: R$ {produto['valor']}")

        compra.append(produto["nome"])
    else:
        print("Opção inválida.")

    input("\nPressione ENTER para voltar ao menu...")
    return


def Finalizar():
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
        input("\nPressione ENTER para voltar ao menu...")
        return


def calcular_ingressos():  #ta certo
    # 1. Definir preços

    precos = {
        "1": {"tipo": "Inteira", "valor": 50.0},
        "2": {"tipo": "Meia-entrada", "valor": 25.0}
    }

    combo_pipoca = 20.0

    total = 0.0
    pedidos = []
    assentos_escolhidos = []

    print("--- Sistema de Venda de Ingressos ---")
    
    while True:
        print("\nEscolha o tipo de ingresso:")
        print("1 - Inteira (R$ 50,00)")
        print("2 - Meia-entrada (R$ 25,00)")
        print("0 - Finalizar compra retornando ao menu principal")
        
        opcao = input("Opção: ")
        
        if opcao == "0": #<<modificado
           return
        elif opcao in precos:
            try:
                qtd = int(input(f"Quantos ingressos de {precos[opcao]['tipo']}? "))
                if qtd > 0:

                 for i in range(qtd):
                        assento = input(f"Escolha o assento do ingresso {i+1}: ")
                if assento not in assentos_escolhidos:
                   assentos_escolhidos.append(assento)
                else:
                    print("Assento já escolhido!")
                    continue
                valor_item = precos[opcao]["valor"] * qtd
                total += valor_item
                pedidos.append(f"{qtd}x {precos[opcao]['tipo']} - R$ {valor_item:.2f}")
                compra.append(f"{qtd}x {precos[opcao]['tipo']} - R$ {valor_item:.2f}")
                print(f"{qtd} {precos[opcao]['tipo']}(s) adicionado(s).")
                pipoca = input("Gostaria de adicionar um combo de pipoca? (sim/não): ").lower()
                if pipoca == "sim":
                   total += combo_pipoca
                   pedidos.append(f"1x Combo de Pipoca - R$ {combo_pipoca:.2f}")
                   compra.append(f"1x Combo de Pipoca - R$ {combo_pipoca:.2f}")
                   print("Combo de pipoca adicionado!")
                else:
                    print("Quantidade inválida.")
            except ValueError:
                print("Por favor, digite um número inteiro.")
        else:
            print("Opção inválida, tente novamente.")

    cupom = input("\nDigite um cupom de desconto (ou ENTER para pular): ").upper()

    if cupom == "DESCONTO10":
        desconto = total * 0.10
        total -= desconto

        print(f"Cupom aplicado! Desconto de R$ {desconto:.2f}")
    else:
        if cupom != "":
            print("Cupom inválido.")

    # 3. Exibir resumo
    print("\n--- Resumo da Compra ---")
    for item in pedidos:
        print(item)

    print(f"Total a pagar: R$ {total:.2f}")
    input("\nPressione ENTER para voltar ao menu...")
    return 
# Executar o sistema


class Usuario:
    #Construtor
    def __init__(self,nome):
        self.nome = nome

ListaUsuario = []
ListaAdmin = []


class Admin(Usuario):
    def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                usuario = str(input("Digite o nome do Usuario"))

                p = Usuario(usuario)
                ListaUsuario.append(p)
                
            else:
                x = False
                input("\nPressione ENTER para voltar ao menu...")
            return


def menuUI():

  while True:

   print("Escolha uma Opcao")
   print("1 - comprar online")
   print("2 - pagar")
   print("3 - finalizar compra")
   print("4 - adicionar usuario")
   print("5 - encerrar")

   escolha = int(input("Digite um numero, para Escolher"))

   if escolha == 1:
      escolha_filme()
   elif escolha == 2:
       calcular_ingressos()
   elif escolha == 3:
       Finalizar()
   elif escolha == 4:
       Admin.adicionar()
   elif escolha == 5:
       print("Encerrando sistema...")
       exit()
   else:
      print("error")

menuUI()