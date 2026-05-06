# =========================
# PARTE 1 - INPUT E PRINT
# =========================

nome = input("Digite seu nome: ")
print("Olá", nome)

# =========================
# PARTE 2 - CONCATENAÇÃO
# =========================

a = ("João")
b = ("Silva")

print(a + " " + b)

# =========================
# PARTE 3 - EQUAÇÃO MATEMÁTICA
# =========================

pedido1 = int(input("escolha um numero: ")) #<< "int" e essencial para a soma
pedido2 = int(input("escolha outro numero: "))

# Soma
print(pedido1 + pedido2)

# Subtração
print(pedido1 - pedido2)

# Multiplicação
print(pedido1 * pedido2)

# Divisão
print(pedido1 / pedido2)

# =========================
# PARTE 4 - FOR
# =========================


numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for numeros in numeros:
    print(numeros)

# =========================
# PARTE 5 - LISTA
# =========================


nomes = ["vinnicios13", "ney", "nosfa"]
print(nomes)

# =========================
# PARTE 6 - DICIONÁRIO
# =========================

user = {
    "nome":"Arthur",
    "idade":15,
    "cidade":"Riacho Fundo 2"
}
print(user)

# =========================
# PARTE 7 - CLASSE E OBJETO
# =========================

class Pessoa:
    def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade
    
    def Logar(self):
          print("oi eu sou " + self.nome)
          print("e eu tenho " + str(self.idade))
p1 = Pessoa("Arthur", 15)
p1.Logar()

# =========================
# PARTE 8 - DESAFIO FINAL
# =========================

# Crie um sistema simples que use TUDO:

# 1. Crie uma classe Pessoa (nome, idade)
# 2. Crie uma lista para guardar pessoas
# 3. Use um while com menu:

#Classe Pai
class Usuario:
    #Construtor
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    def logar(self):
        print("Logou")

    def deslogar(self):
        print("sair da conta")

#Classe Pai
class Usuario:
    #Construtor
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def Saudacoes(self):
          print("oi eu sou " + self.nome)
          print("e eu tenho " + str(self.idade))

ListaUsuario = []
ListaAdmin = []

    
#Classe Filho
class Admin(Usuario):
    def adicionar():
        x = True
        while x == True:
            add = input("Voce gostaria de adicionar um Usuario? s/n")
            if add == "s":
                usuario = str(input("Digite o nome do Usuario"))
                idade = int(input("Digite uma idade do Usuario"))

                p = Usuario(usuario, idade)
                ListaUsuario.append(p)
                
            else:
                x = False
                Admin.menuUI()

    def listar():
        print(ListaUsuario)

    
    def menuUI():
        print("Escolha uma Opcao")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - parar")

        escolha = int(input("Digite um numero, para Escolher"))

        if escolha == 1:
            Admin.adicionar()
        elif escolha == 2:
            Admin.listar()
        if escolha == 3:
           print("encerrando...")
           exit()
        else:
            print("error")

Admin.menuUI()