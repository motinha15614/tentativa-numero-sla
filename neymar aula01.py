# #comando print

# print("ola mundo")
# print("neymar")

# #criação de variante

# x = 15
# y = "sla"
# print(x)

# #if

# nota1 = 2
# nota2 = 9
# media = nota1 + nota2
# print(media)

# if media <= 7 :
#     print("REPROVADO VAI PRA CRECHE  -1000 DE AURA")
# else :
#     print("parabens +100 de aura ;)")

# #sistema simples de login

# nome = input("digite um nome:")
# print(nome)

# print("bem vindo",nome)
# numero = 1
# print("criar conta")

# nome = input("qual o seu nome")
# senha = ("qual a sua senha")

# if(nome == ""):
#     print("não pode ser vazio")
# else:
#     print("bem vindo", nome)
#aula 03

lista = ["ney","cr7","mi"]
print(lista)

menu = ["mcdonalds","bigmac","hamburguer","refri"]
print(len(menu)) #<<serve para contar quantos itens tem na lista
print(menu[1]) 
print(menu)

#remover item da lista
menu.remove("refri")
#adicionar item da lista
menu.append("pizza")

#loop de item
for x in menu:
    print(x)
print(menu)

#nova lista 
listaA = ["A","B","C","D"]
listaB = ["1","2","3","4"]
#juntando duas listas 
listaconjunta = listaA + listaB
print(listaconjunta)
#copiando uma lista
copia = listaconjunta.copy()
#removendo
copia.remove("A")
print(copia) 

#atividade aula 04

fruits = ["maçã","banana","cereja"]
print(fruits[1])
print(len(fruits))

#dicionarios python

pessoa = {
         "nome": "Paulo",
         "idade": 29,
         "filhos": ["João", "Maria"]
}
print(pessoa)

print(pessoa['nome'])

#dicionarios não podem ter dois itens com a mesma chave:
#Exemplo Valores duplicados sobrescreverão os valores existentes:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#aula 04 - while e for


#se repetindo infinitamente até que a palavra "sair"  para acionar o comando "break"

while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == 'sair':
       break

#Classe-aula 06
class Inimigos:
    vida = 100
    dano = 15
    velocidade = 10
    forca = 2

class Player:
    vida = 100
    dano = 15
    velocidade = 10
    forca = 2

#aula 07
