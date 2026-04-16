#comentario ou anotação "#"

#variavel de texto
import email


linha = "texto"
print(linha)

#variavel de numero
multiplicacao = 2
numero1 = 3
multiplo = multiplicacao * numero1

#variavel de numero
numero = 2
print(numero)

#condicional
# > = maior do que
# < = menor do que
# == = exatamente a mesma coisa
# >= = maior e igual do que
# <= = menor e igual do que

if numero ==2:
    print("o seu numero e 2")
if numero >=2:
    print("o seu numero pode ser acima de 2")
if numero <=2:
    print("o seu numero pode ser 2 ou menor")
if numero <2:
    print("o seu numero e menor que 2")
if numero >2:
    print("o seu numero e maior que 2")

    #input criar uma mensagem na terminal

usuario = input("digite um nome:")
print("seja bem vindo",usuario)

#sistema simples de login(teste)

nome = input("e novo aqui? resposta:")
if( nome == "sim" ):
    print("crie uma conta gratis")
else:(nome == "nao")
print("preecha os seguintes espacos")
usuario = input("qual o seu nome:")
senha = input("qual a sua senha:")
#sla
print("bem vindo,")
numero = 1
print("criar conta")

if(nome == ""):
    print("preencha o espaco vazio")
else:
    print("bem vindo",usuario)

#aula 03
#funcao

def funcao():
    print("executa uma ação")

#exemplo

print("ola,bem vindo")
print("Escolha uma Opcao")
print("digite 01 - para criar uma conta")
print("digite 02 - para logar uma conta")
escolha = input("Digite um numero")

def criar():
    usuario = input ("digite seu nome")
    print("Sua conta foi criada",usuario)

def logar():
    print("voce logou")

if escolha == 1:
    criar()
else:
    logar()

def opcao(compra):
    #switch case
    match compra:
        case "Coxinha":
            return "comprar coxinha"
        case "Pastel":
            return "comprar pastel"
        case "refri":
            return "comprar refri"
        case _:
            return "voce nao quer comprar nada"