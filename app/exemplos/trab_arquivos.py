#import subprocess
import os

#arquivo = open("app\exemplos\dados.txt","r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close
#leitura
try:
    with open("app\exemplos\dados.txt","r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileExistsError:
    print("Arquivo não encontrado")

#sobreescrita
with open("app\exemplos\dados.txt","w") as arquivo:
    arquivo.write("Bem vindo ao python")

#adicionar novo conteúdo
with open("app\exemplos\dados.txt","a") as arquivo:
    arquivo.write(" Usuário logado\n")

#abrindo em uma da minha escolha
os.startfile("app\exemplos\dados.txt")
#subprocess.Popen(["code","app\exemplos\dados.txt"])