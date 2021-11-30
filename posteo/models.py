from django.db import models

class posteo(models.Model):
    base = models.CharField(max_length=50)
    fecha = models.DateField(auto_created=True)
    hora_inicio = models.CharField(max_length=6)
    hora_termino =  models.CharField(max_length=6) 
    tipo_brigada = models.CharField(max_length=25)
    clave_de_unidad = models.IntegerField()
    nombre_jefebrigada = models.CharField(max_length=45)
    nombre_conductor = models.CharField(max_length=45)
    numero_de_brigadistas = models.IntegerField()
    numero_de_motosierristas =models.IntegerField()
    numero_de_conductor = models.IntegerField()
    personal_operativo = models.IntegerField()
    patente = models.CharField(max_length=10)
    motosierra = models.BooleanField()
    motobomba = models.BooleanField()
    stock_aero_base = models.IntegerField()
    kit_meteorologico = models.BooleanField()
    sector = models.CharField(max_length=50)
    stock_despuma = models.IntegerField()
    observaciones = models.TextField()

    def __str__(self):
        return self.base
