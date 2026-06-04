#criando base(planta do objeto)
class Carro:
    def __init__(self,moto,quant_rodas):
        self.moto = moto
        self.quant_rodas = quant_rodas
    
    #def __init__(self):
    #    pass

    def andar(self):
        print("carro está andando")

#Sem valores obrigatórios
class Conta:
    def __init__(self):
        pass

#iniciar classe com valores padrão
class Funcionario:
   nome = ""
   idade = 0
   cargo ="" 

#criando objeto
car1 = Carro("v8",4)
car2 = Carro("V6",4)
'''car3 = Carro() #criando carro 3
car3.moto = "V12" #atribuindo o valor a propriedade do objeto
print(car3.moto)
car3.andar()'''#executando a função(ação) do objeto
#Mostrar informações do objeto
print("Carro 1 tem o moto: ",car1.moto)
print("Carro 1 tem o moto: ",car2.moto)
class Cliente:
    def __init__(self,nome,cpf,telefone,email):
      self.nome = nome
      self.cpf = cpf
      self.telefone = telefone
      self.email = email

cliente = Cliente(nome="Maria",cpf="108.454.654-35",telefone="(21)99568-6584",email="mari@gmail.com")

print("Nome cliente:",cliente.nome)
print('CPF:',cliente.cpf) 
print('Telefone:',cliente.telefone)
print('E-mail:',cliente.email)

class Aluno:
    def estudar(self):
        for i in range(5):
            print("Estou estudando")
    
    def vouEstudar(self,resposta):
        if resposta =="sim":
            print("Bom estudo!!")
        else:
            print("Acho que melhor você estudar")

aluno = Aluno()
aluno.estudar()
resposta = input("Você vai estudar hoje")
aluno.vouEstudar(resposta)