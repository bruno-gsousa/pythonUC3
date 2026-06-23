def soma(num1,num2):
    total = num1+num2
    return total

def exebirmsg():
    print("Isso é uma função")

def exebirmsg2():
    return "Isso é uma função 2"

#temp = soma()
print(soma(5,15))

print(exebirmsg2())
exebirmsg()

def test(senha):
    if senha =="12154":
        print("senha correta")
    else:
        print("senha incorreta")

test(input("Digite a sua senha:\n"))

def contnum(num):
    for i in range(1,num):
        print(i)

contnum(15)

def contwhile():
    count=0
    while count<3:
        print(count)
        count+=1

contwhile()