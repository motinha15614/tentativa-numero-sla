

#Em Python,
#o comando "for" é uma estrutura de repetição (loop)
#usada para percorrer ou iterar sobre uma sequência (lista, tupla, string) 
#ou outros objetos iteráveis.


#1. Iterando sobre uma Lista 
#Percorre cada elemento de uma lista de itens. 

frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)



#2. Usando range() para Números
#Gera uma sequência de números
#para repetir um código um número definido de vezes. 

# Imprime números de 0 a 4
for i in range(5):
    print(i)


#O while em Python é uma estrutura de repetição (loop) que executa um bloco de código continuamente enquanto uma condição for verdadeira. 
#É ideal para situações onde o número de repetições não é pré-definido, continuando até que a condição se torne falsa.
#É sinônimo de "laço condicional" ou "estrutura de repetição enquanto".

#contador utilizando o while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1 # Essencial para evitar loop infinito


#se repetindo infinitamente até que a palavra "sair" 
#para acionar o comando "break"
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == 'sair':
        break

#QUAL A DIFERENÇA ENTRE OS DOIS???

#for (Finito/Sequencial): 
#Ideal quando você sabe quantas vezes
# o laço deve rodar ou está percorrendo itens.

#while (Condicional/Infinito): 
#Ideal quando a repetição depende de uma condição que muda dentro do loop
#(ex: esperar o usuário digitar 'sair').


#sistema de login com while

user = "oi"
senha_c = "1234"

logado = False
while not logado:
    print("login")
    user1 = input("usuario: ")
    senha1 = input("senha: ")
    if user1 == user and senha_c == senha_c:
      print("tacerto")
      logado = True
else:
    print("taerrado")