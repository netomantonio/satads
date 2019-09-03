from django.db import models

class Participante(models.Model):
    name = models.CharField(max_length=100, help_text='Nome do Participante', blank=False, null=False, verbose_name='Nome')
    email = models.EmailField(help_text='Email do Participante', blank=False, null=False, verbose_name='E-mail')
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True, verbose_name='CPF')

    def __str__(self):
        return self.name
