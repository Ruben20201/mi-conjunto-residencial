# Usamos una versión oficial de Python ligera
FROM python:3.13-slim

# Evita que Python escriba archivos .pyc y almacene en búfer la salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copiar e instalar las librerías de Python desde requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto al contenedor
COPY . /app/

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación en producción usando Gunicorn
# (⚠️ Reemplaza 'mi_conjunto' por el nombre exacto de la carpeta que contiene tu wsgi.py)
CMD gunicorn mi_conjunto.wsgi:application --bind 0.0.0.0:8000