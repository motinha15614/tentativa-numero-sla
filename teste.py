def obter_texto_valido():
    while True:
        # Solicita a entrada do usuário
        texto = input("Digite algo (não pode ser vazio ou só espaços): ")
        
        # .strip() remove espaços em branco no início e no fim
        if texto.strip() != "":
            # Se tiver conteúdo, retorna o texto e sai do loop
            return texto
        else:
            # Se for vazio, avisa e repete o loop
            print("Entrada inválida! Você não preencheu nada.")

# Uso da função
resultado = obter_texto_valido()
print(f"Você digitou: {resultado}")



#sistema de login(feito pelo google)
