# Generated by Django 4.1.1 on 2022-09-27 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_nome_alter_produto_preco_marketing_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variacao',
            old_name='preco_promo',
            new_name='preco_promocional',
        ),
    ]
