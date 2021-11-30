from django import forms
from django.forms import fields, widgets
from .models import posteo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class agregarForm(forms.ModelForm):

    class Meta:
        model = posteo
        #fields = ['base', 'fecha', 'hora_inicio', 'hora_termino', 'tipo_brigada', 'clave_de_unidad', 'nombre_jefebrigada', 'nombre_conductor',  'numero_de_brigadistas', 'numero_de_motosierristas', 'numero_de_conductor', 'personal_operativo', 'patente', 'motosierra', 'motobomba', 'motosierra', 'stock_aero_base', 'kit_meteorologico', 'sector', 'stock_despuma', 'observaciones']
        fields = '__all__'

        widgets =  {
            "fecha": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2" ]
    