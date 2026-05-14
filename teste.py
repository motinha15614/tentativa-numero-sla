#contagem regressiva utilizando "while"

#instataneo
contador = 10
while contador > 0:
    print(contador)
    contador -= 1  # Decrementa a variável em 1
print("Lançamento!")

#contagem
import time

tempo = 5
while tempo >= 0:
    print(tempo)
    time.sleep(1)  # Espera 1 segundo
    tempo -= 1
print("Fim da contagem!")

#contagem regressiva utilizando "for"


import time

# Contagem regressiva na mesma linha
for i in range(5, 0, -1): #<<range(início, fim, passo)
    print(f"Tempo restante: {i} ", end='\r')
    time.sleep(1)
print("Tempo esgotado!   ")

#em lista
import time

# Contagem regressiva de 10 a 1
for i in range(0, 10, 1): #<<range(início, fim, passo)
    print(i)
    time.sleep(1) # Pausa por 1 segundo
print("Fogo! 🚀")

#sistema de login com tres tentativas

tentativas = 3
flag = True
 
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
        break
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


