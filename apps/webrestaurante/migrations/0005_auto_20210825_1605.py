# Generated by Django 2.0.6 on 2021-08-25 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webrestaurante', '0004_auto_20210825_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='fk_Bebidas',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='fk_Comida',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='fk_Postres',
        ),
        migrations.DeleteModel(
            name='Bebidas',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Postres',
        ),
    ]