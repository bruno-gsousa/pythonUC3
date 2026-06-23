def maior(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Os números são iguais."
    
# Testando a função
print(maior(10, 5))  # Saída: 10
print(maior(3, 8))   # Saída: 8
print(maior(5, 5))   # Saída: Os números são iguais.