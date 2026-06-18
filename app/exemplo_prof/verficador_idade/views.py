from django.shortcuts import render

def home(request):
    mensagem = ""
    conteudo = False

    if request.method == "POST":
        idade = int(request.POST.get("idade"))

        if idade >= 18:
            conteudo = True
        else:
            mensagem = "Você é menor de idade. Acesso não permitido."

    return render(
        request,
        "index.html",
        {
            "mensagem": mensagem,
            "conteudo": conteudo
        }
    )