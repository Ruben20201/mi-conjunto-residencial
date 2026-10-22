from django.shortcuts import render, redirect
from .models import Vehiculo, EmpleadoObra, Boletin, ServicioResidente
from .forms import EmpleadoObraForm  # Asegúrate de que forms.py exista en la carpeta core


def inicio(request):
    return render(request, 'core/inicio.html')

def buscar_placa(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Vehiculo.objects.filter(placa__icontains=query)
    return render(request, 'core/buscar_placa.html', {'resultados': resultados, 'query': query})

def buscar_empleados(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = EmpleadoObra.objects.filter(
            nombre__icontains=query
        ) | EmpleadoObra.objects.filter(
            cedula__icontains=query
        )
    else:
        resultados = EmpleadoObra.objects.all()
    return render(request, 'core/empleados_obra.html', {'resultados': resultados, 'query': query})

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados_obra')
    else:
        form = EmpleadoObraForm()
    return render(request, 'core/registrar_empleado.html', {'form': form})

def lista_boletines(request):
    boletines = Boletin.objects.filter(activo=True).order_by('-fecha_publicacion')
    return render(request, 'core/boletines.html', {'boletines': boletines})

def lista_servicios(request):
    query = request.GET.get('q', '')
    if query:
        servicios = ServicioResidente.objects.filter(
            activo=True,
            profesion_o_servicio__icontains=query
        ) | ServicioResidente.objects.filter(
            activo=True,
            nombre_profesional__icontains=query
        )
    else:
        servicios = ServicioResidente.objects.filter(activo=True)
        
    return render(request, 'core/servicios.html', {'servicios': servicios, 'query': query})