from django.db import models

# Create your models here.


class Comida(models.Model):
    pk_comida = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    img = models.URLField(max_length=8000, blank=False, null=False, default='https://i.postimg.cc/sDGPTK60/51706.jpg')

    class Meta:
        verbose_name = 'Comida'
        verbose_name_plural = 'Comidas'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class Bebida(models.Model):
    pk_bebidas = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    img = models.URLField(max_length=8000, blank=False, null=False, default='https://i.postimg.cc/mkDjZsSb/5406010.jpg')

    class Meta:
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class Postre(models.Model):
    pk_postres = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    img = models.URLField(max_length=8000, blank=False, null=False, default='https://i.postimg.cc/8kj0M2v2/3606.jpg')

    class Meta:
        verbose_name = 'Postre'
        verbose_name_plural = 'Postres'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class Menu(models.Model):
    pk_menu = models.AutoField(primary_key=True, null=False, blank=False)
    tiempo_comida = models.CharField(max_length=20, null=False, blank=False)
    fk_Comida = models.ForeignKey(Comida, null=False, blank=False, on_delete=models.CASCADE)
    fk_Bebidas = models.ForeignKey(Bebida, null=False, blank=False, on_delete=models.CASCADE)
    fk_Postres = models.ForeignKey(Postre, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ['tiempo_comida']

    def __str__(self):
        return "{0}".format(self.tiempo_comida)

class empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    salario = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    telefono = models.TextField(max_length=8, blank=True, null=True)
    direccion = models.TextField(blank=False, null= False)
