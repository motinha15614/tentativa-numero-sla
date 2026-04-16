def logar():
    print("Voce logou")
#atividade
print("BEM VINDO A PIZZARIA CALABRESA GRANDE")

nome = input("e novo aqui? resposta:")

if(nome == "nao"):
    print("preecha os seguintes espacos")
    usuario = input("qual o seu nome:")
    senha = input("qual a sua senha:")

if( nome == "sim" ):
    print("crie uma conta gratis")
    usuario = input("nome de usuario:")
    senha = input("crie uma senha:")
    email1 = input("qual o seu e-mail:")


    if(usuario == ""):
        if( senha == ""):
           def obter_texto_valido():
             while True:
                # Solicita a entrada do usuário
                texto = input("preecha todos os espacos")
        
                # .strip() remove espaços em branco no início e no fim
                if texto.strip() != "":
                    # Se tiver conteúdo, retorna o texto e sai do loop
                    return texto
                else:
                    # Se for vazio, avisa e repete o loop
                    print("Entrada inválida! Você não preencheu nada.")
        resultado = obter_texto_valido()
        print(f"bem vindo {resultado}")
    else:
        print("bem vindo", usuario)


if(email1 == ""):
 def obter_texto_valido1():
    while True:
            # Solicita a entrada do usuário
            texto = input("preecha todos os espacos")
            # .strip() remove espaços em branco no início e no fim
            if texto.strip() != "":
                # Se tiver conteúdo, retorna o texto e sai do loop
                return texto
            else:
                # Se for vazio, avisa e repete o loop
                print("Entrada inválida! Você não preencheu nada.")
# Uso da função
resultado = obter_texto_valido1()
print(f"bem vindo {resultado}")  