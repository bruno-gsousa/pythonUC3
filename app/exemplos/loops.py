for numero in range(5):
    print(numero)


for numero in range(0,11,2):
    print(numero)


for numero in range(1,11):
    print(f"5 x{numero} = {5*numero}")

contador = 0
while contador<5:
    print(contador)
    contador += 1
    #contador = contador +1

for numero in range(0):
    if numero == 5:
        break
    print(numero)

for numero in range(10):
    if numero ==5:
        continue
    print(numero)