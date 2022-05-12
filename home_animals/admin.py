''' Admin '''
from django.contrib import admin
from .models import AnimalType, Animal


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    ''' Animal Type '''

    list_display = ('code', 'description')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    ''' Animal '''
    list_display = ('name', 'type', 'slogan', 'description')
