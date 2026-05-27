idade = input("Informe sua idade:")
novaidade = int(idade)
try:
    if novaidade >=18 :
        print("Acesso liberado ao sistema.")
    else:
        print("idade abaixo da liberação")
except ValueError:
    print("Erro ao digitar")