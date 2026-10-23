FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copiar e instalar requerimientos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Comando para iniciar la aplicación
CMD ["gunicorn", "mi_conjunto.wsgi:application", "--bind", "0.0.0.0:8000"]

CMD python manage.py migrate && gunicorn mi_conjunto.wsgi:application --bind 0.0.0.0:8000