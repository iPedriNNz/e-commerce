# Generated by Django 4.1.1 on 2022-09-21 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=8, verbose_name='CEP (somente números)'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF (somente números)'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
