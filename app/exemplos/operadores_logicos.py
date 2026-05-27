"""
op1        logico  op2 
operando1    >     operando2
operando1    >=     operando2
operando1    <     operando2
operando1    <=     operando2
operando1    ==     operando2
operando1    !=     operando2
operação1   not    operação2
operação1     and    operação2
operação1      or    operação2
Resultados valor True/False
"""
num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))

offline = True
print(num1>num2)
print(num1>=num2)
print(num1<num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)
print(num1>num2 and num1==num2)#duas operações verd(V)
print(num1>num2 or num1==num2)#uma operação verd(V)
print(not offline)