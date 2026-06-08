class Teclado:
    def __init__(self,marca,preco,cor):
        self.marca = marca
        self.preco = preco
        self.cor = cor

    def __str__(self):
        return f"Marca: {self.marca}\n Preço:{self.preco} \n Cor:{self.cor}"

    def minhafucao(self):
        return  f"Marca: {self.marca}\n Preço:{self.preco} \n Cor:{self.cor}"
tecladoLogTec = Teclado("LogTec",7.50,"Preto")
print(tecladoLogTec)
tecladoOutro = Teclado("Master",18.50,"Branco")
print(tecladoOutro.minhafucao())

#Herança

class Animal:
    def __init__(self,revestimento_externo):
        self.revestimento_externo = revestimento_externo

    def __str__(self):
        return f"Tipo de revestimento externo: {self.revestimento_externo}"

class Carnivero(Animal):
    def Comer(self):
        print("Esta comendo carne")

class Mamifero(Animal):
    def Comer(self):
        print("Está mamando")

leao = Mamifero("pelo")
print(leao.Comer())