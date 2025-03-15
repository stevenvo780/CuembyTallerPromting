FROM python:3.10-slim

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos al contenedor
COPY . .

# Hacer ejecutable el script principal
RUN chmod +x run_examples.py

# Comando para ejecutar cuando se inicie el contenedor
CMD ["python", "run_examples.py"]
