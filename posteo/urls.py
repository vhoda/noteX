from django.urls import path
from .views import inicio, agregar, modificar, \
    eliminar, login, registro


urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar/', agregar, name="agregar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('login', login, name="login"),
    path('registro/', registro, name="registro")
]
