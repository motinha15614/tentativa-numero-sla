#estudar mais sobre esse tema


ListaUsuario = []
ListaAdmin = []
#Classe Pai
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
#Classe Filho
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
#Classe Filho
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
        print(ListaUsuario)
        removerUsuario = input("Escreve um nome pra remover")
        ListaUsuario.remove = []
        print(ListaUsuario)

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
