from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class resourceComida(resources.ModelResource):
    class Meta:
        model = Comida

class AdminComida(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['tamaño','precio']
    resource_class = resourceComida

admin.site.register(Comida, AdminComida)

###

class resourcePostre(resources.ModelResource):
    class Meta:
        model = Postre

class AdminPostre(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['tamaño','precio']
    resource_class = resourcePostre

admin.site.register(Postre, AdminPostre)

###

class resourceBebida(resources.ModelResource):
    class Meta:
        model = Bebida

class AdminBebida(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['tamaño','precio']
    resource_class = resourceBebida

admin.site.register(Bebida, AdminBebida)


class resourceMenu(resources.ModelResource):
    class Meta:
        model = Menu

class AdminMenu(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['tiempo_comida']
    resource_class = resourceMenu

admin.site.register(Menu, AdminMenu)

