pessoa = {
    "nome": "Ana",
    "cpf": "540.546.455-45",
    "telefone": 2199556656
}
print(pessoa)
print(pessoa["cpf"])
pessoa["nome"] = "Luiz"# alterei o valor
print(pessoa["nome"])

for chave, valor in pessoa.items():
    print(f"Seu {chave} é {valor}")

pessoa.update({"nome": "Jair", "cpf": "54545454545454", "telefone": 2198453565})
print(pessoa)