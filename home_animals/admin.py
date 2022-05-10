from django.contrib import admin
from .models import AnimalType 


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):

    list_display = ('code', 'description')
