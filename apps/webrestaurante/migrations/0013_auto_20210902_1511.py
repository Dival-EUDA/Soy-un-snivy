# Generated by Django 2.0.6 on 2021-09-02 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webrestaurante', '0012_auto_20210901_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='fk_Bebidas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webrestaurante.Bebida'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='fk_Postres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webrestaurante.Postre'),
        ),
    ]