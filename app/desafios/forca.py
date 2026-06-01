import os
palavra_secreta ='perfume'
letra_acertos = ""
numero_tentativas = 0
letras_erradas =''
while True:
    letra_digitada = input("Digite uma letra")
    letra_digitada = letra_digitada.lower()
    numero_tentativas += 1

#Verificar erros
    if letra_digitada in letra_acertos:
        print("você já acertou essa letra")
        continue

    if letra_digitada in letras_erradas:
        print("Você já tentou essa letra")
        continue

#verificar se letra existe
  
    if len(letra_digitada)>1:
        print("Digite apenas uma letra")
        continue
    if letra_digitada in palavra_secreta:
        letra_acertos += letra_digitada
        print("Letra correta")
    else:
        print("Letra incorreta")
        letras_erradas += letra_digitada

#Monta a palavra escondida
    palavra_formada=''
    for letra_acertos in palavra_secreta:
        if palavra_secreta in letra_acertos:
            palavra_formada += palavra_secreta
        else:
            palavra_formada +="*"
    
#exibe informações do jogo     
    print("\n====================================================")
    print('Palavra:',palavra_formada)
    print('Letras erradas:', letras_erradas)
    print('Tentativas',numero_tentativas)
    print('=====================================================\n')

#Verificar Vitoria
    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você Ganhou!')
        print(f"A palavra secreta era:{palavra_secreta}")
        print(f"Total de tentativas:{numero_tentativas}")

        break
print('\n Jogo encerrado.')