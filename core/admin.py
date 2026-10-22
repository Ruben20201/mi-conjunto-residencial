from django.contrib import admin
from .models import PerfilResidente, Vehiculo, EmpleadoObra, Boletin
from django.contrib import admin
from .models import PerfilResidente, Vehiculo, EmpleadoObra
from .models import PerfilResidente, Vehiculo, EmpleadoObra, Boletin, ServicioResidente

admin.site.register(PerfilResidente)
admin.site.register(Vehiculo)
admin.site.register(EmpleadoObra)
admin.site.register(Boletin)
admin.site.register(ServicioResidente) 



 