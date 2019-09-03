from django.db import models

from apps.eventos.models import Evento


class Atracao(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da atração', blank=False, null=False, verbose_name='Nome')
    horario = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural='Atrações'
        verbose_name='Atração'

    def __str__(self):
        return self.name
