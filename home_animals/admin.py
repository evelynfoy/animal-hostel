"""
    Registers all the models for the home_animals application
"""
from django.contrib import admin
from .models import AnimalType, Animal, Offer


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    ''' Animal Type '''
    list_display = ('code', 'description')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    ''' Animal '''
    list_display = ('name', 'type', 'slogan', 'description')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    ''' Offer '''
    list_display = ('animal', 'user', 'basis', 'status', 'weeks')
