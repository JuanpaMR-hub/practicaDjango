from django.contrib import admin
from . import models


@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre','edad']
