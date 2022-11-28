from django.shortcuts import render, redirect
from .models import Palestrante, Palestras, Inscricoes

def home(request):
    return render(request, "index.html")

def salvarPalestrante(request):
    vnome = request.POST.get("nome")
    Palestrante.objects.create(nome=vnome)
    palestrantes = Palestrante.objects.all()
    return render(request, "index.html", {"palestrantes": palestrantes})

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

def salvarPalestras(request):
    vnome = request.POST.get("nome")
    Palestras.objects.create(nome=vnome)
    palestras = Palestras.objects.all()
    return render(request, "index.html", {"palestras": palestras})

def editarPalestras(request, id):
    palestra = Palestras.objects.get(id=id)
    return render(request, "update.html", {"palestra": palestra})

def updatePalestras(request, id):
    vnome = request.POST.get("nome")
    palestras = Palestras.objects.get(id=id)
    palestras.nome = vnome
    palestras.save()
    return redirect(home)

def excluirPalestras(request, id):
    palestras = Palestras.objects.get(id=id)
    palestras.delete() 
    return redirect(home)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def salvarInscricoes(request):
    vnome = request.POST.get("nome")
    Inscricoes.objects.create(nome=vnome)
    inscricoes = Inscricoes.objects.all()
    return render(request, "index.html", {"inscricoes": inscricoes})

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




