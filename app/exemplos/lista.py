nome = "bruno"
listaNomes = ["Bruno","Maria","Marta","Luiz","Rafael"]
print(nome)
print(listaNomes)
print(len(listaNomes))#contar quantos elementos existem
listaNomes.append("Ana") # adiciona um novo item na lista
print(listaNomes)
print(listaNomes.index("Bruno")) #recuperar o index da pesquisa
nova_lista = [1,5,"Kyo","Iory"] # lista heterogênea
print(nova_lista)
#nova_lista.remove(5)#remover item da lisa
#nova_lista.remove("Kyo")
nova_lista.reverse()
print(nova_lista)
nova_lista.append([10,56,9])#adiciona uma lista dentro de outra lista
print(nova_lista)
mercado =["Arroz","Maçã","Ovo","cenoura","uva"]
print("arroz" in mercado) #Arrroz está na lista Mercado
print(mercado[4]) #retorna o primeiro item da lista
print("uva" not in mercado) #Verifica 'uva' não está na lista
print(mercado[-1])
print(mercado[-5])
numeros = [5,3,1,4,2]
#print(numeros.sort())# Ordenando crescente
#numeros.sort(everse=True) # Ordenado Decrescente

listaNumero2 = numeros.copy() #Copiar lista

#fatia lista
n1 = numeros[0]
n2 = numeros[1]
#ou
print(numeros[2:5])

print(numeros.clear) #remove todos itens da lista

#remover elementos da lista
print(numeros.pop(4)) # remover pelo index
del numeros[1]
print(numeros)