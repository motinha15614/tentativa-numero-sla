

#aula 07
#classe
class Pessoa:
    #construtor
 def __init__(self, nome, idade):
    #self = o proprio objeto recebe os valores
   self.nome = nome
   self.idade = idade
 def saudacoes(self):
  print("opa, eu sou " + self.nome)
  print ("e eu tenho " + str(self.idade)) #<<OPCIONAL
#objeto personalizado
p1 = Pessoa("Arthur", 15)
p1.saudacoes()

class Estudante(Pessoa):
    pass
x = Estudante("Maria", 23)
x.saudacoes()

class Falar:
    def Som(self,som):
        print(som)
class Cachorro:
    def Som(self):
        print("O cachorro late: MIAAAAAAAAAAAAAUUUUUUUUU")
class Gato:
    def Som(self):
        print("O gato mia: AU AU AU")

p1 = Cachorro()
p1.Som()
p2 = Gato()
p2.Som()

class Entrega:
    def __init__(self, nome, pais, cep, cpf):
        self.nome = nome
        self.pais = pais
        self.cep = cep
        self.cpf = cpf

lista = []
continuar = "s"

while continuar == "s":
    nome = input("digite o nome do de usuario: ")
    pais = (input("qual o seu pais: "))
    cep = (input("qual o seu CEP: "))
    cpf = (input("qual o seu CPF: "))

    p = Entrega(nome, pais, cep, cpf)
    lista.append(p)
    continuar = input("deseja fazer um pedido? s/n: ")

    for entrega in lista:
        print("nome:", entrega.nome)
        print("pais:", entrega.pais)
        print("cep:", entrega.cep)
        print("cpf:", entrega.cpf)



 #Classe Pai

ListaUsuario = []
ListaAdmin = []

class Usuario:
    #Construtor
    def __init__(self,nome,senha,cpf,email):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.email = email

    def logar(self):
        print("Logou")

    def trocarConta(self):
        print("Trocou de Conta")

    def deslogar(self):
        print("sair da conta")

class Cliente(Usuario):
    def Comentar():
        comentario = input("Digite um comentario")
        print(comentario)

    def Curtir():
        curtir = input("Deseja Curtir? s/n")
        if curtir == "s":
            print("Curtida executada")
        else:
            print("Curtida Cancelada")

    def Postar():
        postar = input("Deseja Curtir? s/n")
        if postar == "s":
            print("Postagem feita")
        else:
            print("Postagem Cancelada")

    def Filtrar():
        print("Filtrar qualquer coisa")

class Admin(Usuario):
    def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                usuario = str(input("Digite o nome do Usuario"))
                senha = int(input("Digite uma senha do Usuario"))
                cpf = str(input("Digite o CPF do Usuario"))
                email = str(input("Digite o CPF do Usuario"))
                
                p = Cliente(usuario, senha, cpf, email)
                ListaUsuario.append(p)
                
            else:
                x = False
                Admin.menuUI()

    def remover():
        print("Remover conta")

    def alterar():
        print("alterar conta")

    def listar():
        print(ListaUsuario)

    def menuUI():
        print("Escolha uma Opcao")
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Alterar")
        print("4 - Listar")

        escolha = int(input("Digite um numero, para Escolher"))

        if escolha == 1:
            Admin.adicionar()
        elif escolha == 2:
            Admin.remover      
        elif escolha == 3:
            Admin.alterar()
        elif escolha == 4:
            Admin.listar()
        else:
            print("error")

Admin.menuUI()