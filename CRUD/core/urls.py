from django.contrib import admin
from django.urls import path
from .views import home,palestras,inscricao,cadastroPalestras,cadastroInscricao, salvar,editarPalestrante,updatePalestrante,excluirPalestrante,salvarInscricoes,editarInscricoes,updateInscricoes,excluirInscricoes

urlpatterns = [
    path('', home),
    path('palestras', palestras),
    path('inscricao', inscricao),
    path('cadastroPalestras', cadastroPalestras),
    path('cadastroInscricao',cadastroInscricao),
    
    path('salvar/',salvar, name="salvar"),
    path('editarPalestrante/<int:id>', editarPalestrante, name="editar"),
    path('updatePalestrante/<int:id>', updatePalestrante, name="update"),
    path('excluirPalestrante/<int:id>', excluirPalestrante, name="excluir"),

    
    path('salvarInscricoes/', salvarInscricoes, name="salvarInscricoes"),
    path('editarInscricoes/<int:id>', editarInscricoes, name="editar"),
    path('updateInscricoes/<int:id>', updateInscricoes, name="update"),
    path('excluirInscricoes/<int:id>', excluirInscricoes, name="excluir"),
    

]
