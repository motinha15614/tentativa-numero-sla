def logar():
    print("Voce logou")
#atividade
print("BEM VINDO A PIZZARIA CALABRESA GRANDE")

nome = input("e novo aqui? resposta:")

if(nome == "nao"):
    print("preecha os seguintes espacos")
    usuario = input("qual o seu nome:")
    senha = input("qual a sua senha:")
    if(usuario and senha == ""):
         print("bem vindo",usuario)
    else:
         print("bem vindo",usuario)


if( nome == "sim" ):
    print("crie uma conta gratis")
    usuario = input("nome de usuario:")
    senha = input("crie uma senha:")
    email1 = input("qual o seu e-mail:")


if(usuario == ""):
    if( senha == ""):
        if( email1 == ""):
           def obter_texto_valido():
             while True:
                # Solicita a entrada do usuário
                texto = input("preecha todos os espacos")

    print("Entrada inválida! Você não preencheu nada.")
    resultado = obter_texto_valido()
    print(f"bem vindo {resultado}")
else:
    print("bem vindo", usuario)