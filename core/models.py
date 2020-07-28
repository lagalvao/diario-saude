from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


#Criacao das tabelas do banco de dados
class Farmaco(models.Model):
    substancias = models.CharField(max_length=200)

    def __str__(self):
        return self.substancias


class GrupoFarmacoII(models.Model):
    substancia = models.CharField(max_length=100)

    def __str__(self):
        return self.substancia


class GrupoFarmaco(models.Model):
    substancia = models.CharField(max_length=100)

    def __str__(self):
        return self.substancia


class Intensidade(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Classificacao(models.Model):
    tipo = models.CharField(max_length=1)

    def __str__(self):
        return self.tipo


class Remedio(models.Model):
    nome_cientifico = models.CharField(max_length=50)
    grupo_farmacoI = models.ForeignKey(GrupoFarmaco, on_delete=models.CASCADE)
    grupo_farmacoII = models.ForeignKey(GrupoFarmacoII, on_delete=models.CASCADE)
    farmacos = models.ManyToManyField(Farmaco)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    efeito = models.TextField(max_length=200)
    intensidade = models.ForeignKey(Intensidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cientifico


class Historico(models.Model):
    usuario = models.IntegerField()
    remedio = models.CharField(max_length=50)


class Analise(models.Model):
    usuario = models.IntegerField()
    remedio = models.IntegerField()


class Controle(models.Model):
    usuario = models.IntegerField()
    titulo = models.CharField(max_length=30)
    cor = models.CharField(max_length=15)
    data_inicio = models.CharField(max_length=100, null=True, blank=True)
    data_fim = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titulo