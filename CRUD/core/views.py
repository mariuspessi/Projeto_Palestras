from django.shortcuts import render, redirect
from .models import Palestrante, Inscricoes

def home(request):
    return render(request, "index.html")

def palestras(request):
    palestrantes = Palestrante.objects.all()
    return render(request, "palestras.html",{"palestrantes ": palestrantes})

def cadastroPalestras(request):
    return render(request, "cadastroPalestrantes.html")

def inscricao(request):
    return render(request, "inscricao.html")

def cadastroInscricao(request):
    return render(request, "cadastroIncricoes.html")

def salvar(request):
    vnome = request.POST.get("nome")
    Palestrante.objects.create(nome=vnome)
    palestrantes = Palestrante.objects.all()
    return render(request, "palestras.html", {"palestrantes": palestrantes})

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
    vCPF = request.POST.get("CPF")
    vdata = request.POST.get("data_nascimento")
    Inscricoes.objects.create(nome=vnome,CPF=vCPF,data_nascimento=vdata)
    inscricoes = Inscricoes.objects.all()
    return render(request, "cadastroincricoes.html", {"inscricoes": inscricoes})

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




