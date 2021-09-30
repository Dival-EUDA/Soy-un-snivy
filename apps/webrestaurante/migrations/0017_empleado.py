# Generated by Django 2.0.6 on 2021-09-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webrestaurante', '0016_auto_20210909_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('pk_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('telefono', models.TextField(blank=True, max_length=8, null=True)),
                ('direccion', models.TextField()),
            ],
        ),
    ]
