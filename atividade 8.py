compra = []
pedidos = []

def calcular_valor():  #ta certo
    # 1. Definir preços

    precos = {
        "1": {"tipo": "Inteira", "valor": 50.0},
        "2": {"tipo": "Meia-entrada", "valor": 25.0}
    }

 
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
                    valor_item = precos[opcao]["valor"] * qtd
                    total += valor_item
                    pedidos.append(f"{qtd}x {precos[opcao]['tipo']} - R$ {valor_item:.2f}")
                    compra.append(f"{qtd}x {precos[opcao]['tipo']} - R$ {valor_item:.2f}")
                    print(f"{qtd} {precos[opcao]['tipo']}(s) adicionado(s).")
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

#obs:na progamacao os codigos sao lidos de cima para baixo
class Usuario:
    #Construtor
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

tentativas = 3
flag = True
def cadastrar():
    nome = input("qual sera o seu nome: ")
    senha = input("qual sera a sua senha: ")


def Login():
    while True:
 
        if flag:
          username = input("Entre com seu nome de usuario: ")
 
        if username == 'neymar':
 
          if flag:
            tentativas = 3
          flag = False
 
          password = input("Entre com sua senha: ")
     
          if password == 'senha':
            print("login realizado")
            print(f"seja bem vindo",username)
            menuUI()
          else:
            print("Incorrect password")
        else:
          print("Incorrect username")
 
        tentativas -= 1
 
        print(f"voce só tem mais {tentativas} tentativas")
 
        if tentativas == 0:
            print("se e loco muito burro")
            print("ACESSO NEGADO")
            break


print("bem vindo ao SUPERMERCADO PAGUE MAIS LEVE MENOS!!!")

alimentos = ["0-arroz","1-ps5","2-abacaxi","3-hidrogen bomb","4-coxinha"]
escolha = ("qual alimento voce gostaria comprar:")

ListaUsuario = []
ListaAdmin = []

if(escolha == "0"):
    print(alimentos[0])

if(escolha == "1"):
    print(alimentos[1])
   
if(escolha == "2"):
    print(alimentos[2])
   
if(escolha == "3"):
    print(alimentos[3])

if(escolha == "4"):
    print(alimentos[4])
   
def adicionar():

 def listar():
       print(alimentos)  
       input("\nPressione ENTER para voltar ao menu...")
       return

def menuUI():

  while True:

   print("Escolha uma Opcao")
   print("1 - cadastrar produto")
   print("2 - pagar")
   print("3 - finalizar compra")
   print("4 - encerrar")
   print("5 - Relatório")
   print("6 - Sair")

   escolha = int(input("Digite um numero, para Escolher"))


   if escolha == 1:
       adicionar()
   elif escolha == 6:
       print("Encerrando sistema...")
       exit()
   else:
      print("error")

menuUI()





input("\nPressione ENTER para voltar ao menu...")
return
