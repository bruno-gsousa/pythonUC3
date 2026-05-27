import os
palavra_secreta ='perfume'
letra_acertos = ""
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra")
    numero_tentativas += 1

    if len(letra_digitada)>1:
        print("Digite apenas uma letra")
        continue
    if letra_digitada in palavra_secreta:
        letra_acertos += letra_digitada

    palavra_formada = ""