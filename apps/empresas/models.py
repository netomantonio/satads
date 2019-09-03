from django.db import models

from apps.eventos.models import Evento


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Empresa')
    eventos = models.ManyToManyField(Evento)

    def __str__(self):
        return self.nome