from django.db import models

# Create your models here.


class Comida(models.Model):
    pk_comida = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)

class Bebida(models.Model):
    pk_bebidas = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)

class Postre(models.Model):
    pk_postres = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)

class Menu(models.Model):
    pk_menu = models.AutoField(primary_key=True, null=False, blank=False)
    tiempo_comida = models.CharField(max_length=20, null=False, blank=False)
    fk_Comida = models.ForeignKey(Comida, null=False, blank=False, on_delete=models.CASCADE)
    fk_Bebidas = models.ForeignKey(Bebida, null=False, blank=False, on_delete=models.CASCADE)
    fk_Postres = models.ForeignKey(Postre, null=False, blank=False, on_delete=models.CASCADE)

