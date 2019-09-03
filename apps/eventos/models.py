from django.db import models

class Evento(models.Model):
    name = models.CharField(max_length=100, help_text='Nome do Evento', verbose_name='Nome', blank=False, null=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
