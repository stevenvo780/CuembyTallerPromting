# Proyecto Talleres Cuemby

Este proyecto contiene ejemplos de integración de LangChain con OpenAI usando OpenRouter, incluyendo:
- Ejecución secuencial de ejemplos (`run_examples.py`)
- Servicio API con Flask (`api_service.py`)
- Diversos scripts de ejemplo para pruebas de modelos y funcionalidades específicas

## Requisitos

- Python 3.x
- Dependencias listadas en [requirements.txt](./requirements.txt)
- Archivo de variables de entorno [.env]

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno en el archivo `.env`.

## Uso

### Modo API

Ejecuta el servicio API:
```bash
python entrypoint.py api
```
Accede a la API en [http://0.0.0.0:5000](http://0.0.0.0:5000).

### Modo Batch

Ejecuta todos los ejemplos de manera secuencial:
```bash
python entrypoint.py batch
```

## Scripts Principales

- `base.py`: Ejemplo básico de invocación de un modelo.
- `temp.py`: Pruebas de diferentes temperaturas en las respuestas.
- `systemPromt.py`: Uso de mensajes del sistema para controlar la salida.
- `keto_classification.py`: Clasificación de listas de compras como keto o no keto.
- `few_shot_prompting.py`: Clasificación de correos usando few-shot prompting.
- `few_shot_lista_de_compras.py`: Conversión de unidades en listas de compras.
- `fechas_format.py`: Formateo de fechas en texto a formato YYYY/M/D.
- `factura_extractor.py`: Extracción estructurada de información de facturas.
- `chain_of_thought_example.py`: Resolución de problemas matemáticos paso a paso.
- `clasificacion_sentimientos.py`: Análisis de sentimientos en tweets.

## Notas

- Asegúrate de tener la llave API correcta en `.env`.
- Revisa cada script para entender el flujo específico de cada ejemplo.

