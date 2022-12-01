from django.shortcuts import render, redirect
from .models import Palestrante, Inscricoes

def home(request):
    return render(request, "index.html")

def palestras(request):
    palestrantes = palestrantes.objects.all()
    return render(request, "palestrante.html",{"palestrantes ": palestrantes})

def cadastroPalestras(request):
    return render(request, "cadastroPalestrantes.html")

def inscricao(request):
    return render(request, "inscricao.html")

def cadastroInscricao(request):
    return render(request, "cadastroIncricoes.html")

def salvar(request):
    vpalestra = request.POST.get("palestra")
    Palestrante.objects.create(palestra=vpalestra)
    palestrantes = Palestrante.objects.all()
    return render(request, "palestras.html", {"palestrantes": Palestrante})

def editarPalestrante(request, id):
    palestrante = Palestrante.objects.get(id=id)
    return render(request, "update.html", {"palestrante": palestrante})

def updatePalestrante(request, id):
    vnome = request.POST.get("nome")
    palestrantes = Palestrante.objects.get(id=id)
    palestrantes.nome = vnome
    palestrantes.save()
    return redirect(home)

def excluirPalestrante(request, id):
    palestrantes = Palestrante.objects.get(id=id)
    palestrantes.delete() 
    return redirect(home)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def salvarInscricoes(request):
    vnome = request.POST.get("nome")
    Inscricoes.objects.create(nome=vnome)
    inscricoes = Inscricoes.objects.all()
    return render(request, "inscricao.html", {"inscricoes": inscricoes})

def editarInscricoes(request, id):
    inscricoes = Inscricoes.objects.get(id=id)
    return render(request, "update.html", {"inscricoes": inscricoes})

def updateInscricoes(request, id):
    vnome = request.POST.get("nome")
    inscricoes = Inscricoes.objects.get(id=id)
    inscricoes.nome = vnome
    inscricoes.save()
    return redirect(home)

def excluirInscricoes(request, id):
    inscricoes = Inscricoes.objects.get(id=id)
    inscricoes.delete() 
    return redirect(home)




