from django.forms import *
from parcial.models import *


class RegistroIO(ModelForm):

    class Meta:
        model = Registro
        fields = ['empleado', 'movimiento']

