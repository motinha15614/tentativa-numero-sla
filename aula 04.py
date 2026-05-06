#obs:na progamacao os codigos sao lidos de cima para baixo

print("bem vindo ao SUPERMERCADO PAGUE MAIS LEVE MENOS!!!")

alimentos = ("0-arroz","1-ps5","2-abacaxi","3-hidrogen bomb","4-coxinha")
escolha = ("qual alimento voce gostaria comprar:")

eae = {
         "nome": "arroz",
         "validade": 1958,
}
oi = {
     "nome": "PLAYSTATION 5",
     "validade": "até quebrar"
}
mi = {
     "nome": "abacaxi",
     "validade": 1922
}

oioi = {
     "nome": "hidrogen bomb",
     "validade": 24356
}
err = {
     'nome': "coxinha",
     "validade": "1 dia"
}
print(alimentos)
escolha = input(escolha)

if(escolha == "0"):
    print(alimentos[0])
    print(eae)
if(escolha == "1"):
    print(alimentos[1])
    print(oi)
if(escolha == "2"):
    print(alimentos[2])
    print(mi)
if(escolha == "3"):
    print(alimentos[3])
    print(oioi)
if(escolha == "4"):
    print(alimentos[4])
    print(err)