# Generated by Django 2.2.5 on 2019-09-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome do Participante', max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(help_text='Email do Participante', max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
            ],
        ),
    ]
