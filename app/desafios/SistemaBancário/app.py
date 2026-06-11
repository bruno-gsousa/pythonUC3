#cliente
class Cliente:
    def __init__(self,nome,cpf):
       self.nome = nome
       self.cpf = cpf 
    
    def __str__(self):
        return f"Cadastro realizado:\n nome: {self.nome} cpf: {self.cpf}"


#conta
class Conta:
    def __init__(self,numero,cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
    
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado")
        else:
            print("Valor inválido")
    
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado")
        else:
            print("saldo insuficiente")

    def transferir(self,destino,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Transferência realizada")
        else:
            print("saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo atual R$ {self.saldo}")
    
    def __str__(self):
        return(
            f"Conta:{self.numero}\n"
            f"Titular:{self.cliente.nome}\n"
            f"Saldo: R${self.saldo}"
        )
    
#Herança conta corrente
class ContaCorrente(Conta):
    def __init__(self,numero,cliente,limite):
        super().__init__(numero,cliente)
        self.limite = limite

    def sacar(self, valor):
        if valor <=(self.saldo+self.limite):
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado")
        else:
            print("saldo insuficiente")
    
    def __str__(self):
        return(
            f"Conta:{self.numero}\n"
            f"Titular:{self.cliente.nome}\n"
            f"Saldo: R${self.saldo}\n"
            f"Limite: R$ {self.limite}"
        )
#Herança conta poupança
class ContaPoupanca(Conta):
    def __str__(self):
        return(
            f"Conta poupança:\n "
            f"Conta:{self.numero}\n"
            f"Titular:{self.cliente.nome}\n"
            f"Saldo: R${self.saldo}\n"  
        )

#Programa principal

cliente1 = Cliente("Maria","108.545.454-35")
cliente2 = Cliente("Carlos","106.595.333-85")

conta1 = ContaCorrente(1001,cliente1,500)
conta2 = ContaPoupanca(2001,cliente2)

print("\n====Deposito=====")
conta1.depositar(1200)
conta2.depositar(4500)
print("\n====Saque=====")
conta1.sacar(250)

print("\n====Transferência=====")
conta1.transferir(conta2,200)

print("\n====Saldos=====")
conta1.exibir_saldo()
conta2.exibir_saldo()
