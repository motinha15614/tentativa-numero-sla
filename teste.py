

class Usuario:
    #Construtor
    def __init__(self,nome):
        self.nome = nome

usuarios_cadastrados = {
    "admin": "12345",
    "joao": "senha123",
    "maria": "123"
}

class Admin(Usuario):
    def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                usuario = str(input("Digite o nome do Usuario"))
                senha = str(input("Senha: "))

                p = Usuario(usuario)
                s = Usuario(senha)

                usuarios_cadastrados.append(p)
                usuarios_cadastrados.append(s)
            else:
                x = False
                input("\nPressione ENTER para voltar ao menu...")
            return

# Lista de usuários autorizados
 
    # Verifica se o usuário existe e se a senha corresponde
def entrar():

    username = str(input("Usuário: "))
    password = int(input("Senha: "))

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
        print("2 - entrar")
        print("1 - Adicionar")
        

        escolha = int(input("Digite um numero, para Escolher"))

        if escolha == 1:
            entrar()
        elif escolha == 2:
            Admin.adicionar()
        else:
            print("error")

menuUI()