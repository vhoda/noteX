from django.contrib import admin
from .models import posteo

@admin.register(posteo)
class posteoAdmin(admin.ModelAdmin):
    list_display = ['base', 'fecha', 'hora_inicio', 'hora_termino', 'tipo_brigada', 'clave_de_unidad', 'nombre_jefebrigada', 'nombre_conductor',  'numero_de_brigadistas', 'numero_de_motosierristas', 'numero_de_conductor', 'personal_operativo', 'patente', 'motosierra', 'motobomba', 'motosierra', 'stock_aero_base', 'kit_meteorologico', 'sector', 'stock_despuma', 'observaciones']
     
# Register your models here.
