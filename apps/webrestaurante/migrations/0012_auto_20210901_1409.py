# Generated by Django 2.0.6 on 2021-09-01 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webrestaurante', '0011_auto_20210901_1102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postres',
            new_name='Bebida',
        ),
        migrations.RenameModel(
            old_name='Bebidas',
            new_name='Postre',
        ),
        migrations.RenameField(
            model_name='bebida',
            old_name='pk_postres',
            new_name='pk_bebidas',
        ),
        migrations.RenameField(
            model_name='postre',
            old_name='pk_bebidas',
            new_name='pk_postres',
        ),
    ]