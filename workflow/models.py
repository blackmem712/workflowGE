from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200) 
    cpf = models.CharField(max_length=12) 
    email = models.EmailField(max_length=50)
    endereco = models.TextField()
    cidade = models.CharField(max_length=12)
    telefone = models.CharField(max_length=50) 
    
    def __str__(self) -> str:
        return f'{self.nome}'

 ### "Classes abstratas base" da pra usar aqui para que cliente e funcionário herdem pessoa   ####
 ### link da documentação "https://docs.djangoproject.com/pt-br/4.2/topics/db/models/#abstract-base-classes" #####

class Cliente(models.Model):
  Cliente = models.ForeignKey(Pessoa, on_delete= models.CASCADE)
 
class Funcionario(models.Model):
 funcionario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)



    
    