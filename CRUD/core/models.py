from django.db import models
#from djongo import models

class Palestrante(models.Model):
    palestra = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=100)
    data = models.DateField()
    #hora = models.DateTimeField()
    
    def __str__(self):
        return self.nome
    
class Inscricoes(models.Model):
    nome = models.CharField(max_length=100)
    CPF = models.IntegerField()   
    data_nascimento = models.DateField()
    palestr1 =models.CharField(max_length=100)
    

    
    
   
    
