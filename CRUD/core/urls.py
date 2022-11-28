from django.contrib import admin
from django.urls import path
from .views import home, salvarPalestrante,editarPalestrante,updatePalestrante,excluirPalestrante,salvarPalestras,editarPalestras,updatePalestras,excluirPalestras,salvarInscricoes,editarInscricoes,updateInscricoes,excluirInscricoes

urlpatterns = [
    path('', home),
    path('salvarPalestrante/', salvarPalestrante, name="salvar"),
    path('editarPalestrante/<int:id>', editarPalestrante, name="editar"),
    path('updatePalestrante/<int:id>', updatePalestrante, name="update"),
    path('excluirPalestrante/<int:id>', excluirPalestrante, name="excluir"),
    
    path('salvarPalestras/', salvarPalestras, name="salvar"),
    path('editarPalestras/<int:id>', editarPalestras, name="editar"),
    path('updatePalestras/<int:id>', updatePalestras, name="update"),
    path('excluirPalestras/<int:id>', excluirPalestras, name="excluir"),
    
    path('salvarInscricoes/', salvarInscricoes, name="salvar"),
    path('editarInscricoes/<int:id>', editarInscricoes, name="editar"),
    path('updateInscricoes/<int:id>', updateInscricoes, name="update"),
    path('excluirInscricoes/<int:id>', excluirInscricoes, name="excluir"),
    

]
