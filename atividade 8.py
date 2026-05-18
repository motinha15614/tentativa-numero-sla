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
   print("1 - adicionar produto")
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
