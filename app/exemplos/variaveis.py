nome = "Bruno" #str
idade = 39 #int
altura = 1.73 #float
aluno = False #bool True/False

print("Nome: " + nome)
print(idade)
print(f"Altura: {altura}")#atual
print("Aluno:\n %s"%(aluno))#antigo

print("-----------------------------------------")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(aluno))

print(f"Nome:{nome}\t Idade: {idade} \n altura: {altura} aluno:{aluno}")