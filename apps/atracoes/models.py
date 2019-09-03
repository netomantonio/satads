from django.db import models

class Atracao(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da atração', blank=False, null=False, verbose_name='Nome')
    horario = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)

