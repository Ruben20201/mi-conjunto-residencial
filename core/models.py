from django.db import models

from django.db import models
from django.contrib.auth.models import User

# 1. Perfil asociado al usuario para el Apartamento
class PerfilResidente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartamento = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Apto {self.apartamento} - {self.user.username}"

# 2. Tabla de Vehículos / Placas
class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca_modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    residente = models.ForeignKey(PerfilResidente, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.placa} ({self.marca_modelo})"


# 3. Tabla de Empleados de Obra
class EmpleadoObra(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    arl_vigente = models.BooleanField(default=True)
    apartamento_responsable = models.ForeignKey(PerfilResidente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - C.C. {self.cedula}"


# 4. Tabla de Boletines Informativos
class Boletin(models.Model):
    # ¡Asegúrate de que estas líneas tengan sangría (espacios a la izquierda)!
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# 5. Tabla de Servicios / Directorio Profesional de Residentes
class ServicioResidente(models.Model):
    CATEGORIAS = [
        ('SALUD', 'Salud / Medicina'),
        ('LEGAL', 'Asesoría Legal / Abogados'),
        ('SEGURIDAD', 'Seguridad / Fuerza Pública'),
        ('TECNICO', 'Mantenimiento / Reparaciones'),
        ('EDUCACION', 'Tutorías / Clases'),
        ('OTRO', 'Otros Servicios'),
    ]

    nombre_profesional = models.CharField(max_length=120)
    profesion_o_servicio = models.CharField(max_length=150)  # Ej: "Médico General", "Abogado Penalista"
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTRO')
    apartamento = models.CharField(max_length=20)
    telefono_contacto = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_profesional} - {self.profesion_o_servicio} ({self.apartamento})"