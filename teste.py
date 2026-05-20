

class Usuario:
    #Construtor 
    def __init__(self,nome, senha):
        self.nome = nome
        self.senha = senha

usuarios_cadastrados = []

def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                usuario = str(input("Digite o nome do Usuario: "))
                senha = int(input("Senha: "))

                p = (usuario, senha)
                usuarios_cadastrados.append(p)
            else:
                x = False
                input("\nPressione ENTER para voltar ao menu...")
            return

def entrar(): #ta certo

    username = str(input("Usuário: "))
    password = str(input("Senha: "))

    if username in usuarios_cadastrados and usuarios_cadastrados[username] == password:
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        input("\nPressione ENTER para voltar ao menu...")
    return

def menuUI():
    while True:
        print("Escolha uma Opcao")
        print("1 - entrar")
        print("2 - Adicionar")
        

        escolha = int(input("Digite um numero, para Escolher"))

        if escolha == 1:
            entrar()
        elif escolha == 2:
            adicionar()
        else:
            print("error")

menuUI()