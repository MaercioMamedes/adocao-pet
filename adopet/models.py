from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

UserModel = get_user_model()

class Tutor(models.Model):
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    telefone = models.IntegerField()
    whatsapp = models.IntegerField()
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.id_user.username

class Animal(models.Model):
    id_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    porte = models.CharField(max_length=255)
    peso = models.FloatField()
    tipo_animal = models.CharField(max_length=255)
    idade = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome

class Galeria(models.Model):
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    tipo_arquivo = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.url
