from django.db import models

# Create your models here.



class Movimiento(models.Model):
    tipo = models.CharField(max_length=50)


class Empleado(models.Model):
    nombre = models.CharField(max_length=200, help_text='Tu nombre')
    aPaterno = models.CharField(max_length=50)
    aMaterno = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    celular = models.CharField(max_length=10)

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado,
                                 choices=Empleado.objects.all().values_list('id', 'nombre'))
    fecha = models.DateTimeField(auto_now=True)
    movimiento = models.ForeignKey(Movimiento,

                                   blank=False,
                                   choices=Movimiento.objects.all().values_list('id', 'tipo'))
    foto = models.CharField(max_length=255)
class Prueba(models.Model):
     nombre = models.CharField(max_length=40)