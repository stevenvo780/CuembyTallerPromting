FROM python:3.10-slim

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos al contenedor
COPY . .

# Exponer el puerto para la API
EXPOSE 5000

# Por defecto, iniciar la API usando Python directamente
CMD ["python", "entrypoint.py"]
