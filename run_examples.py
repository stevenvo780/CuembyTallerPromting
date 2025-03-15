import os
import time
import sys

def run_script(script_path, description):
    print("\n" + "="*80)
    print(f"Ejecutando: {script_path}")
    print(f"Descripción: {description}")
    print("="*80 + "\n")
    
    os.system(f"python {script_path}")
    
    print("\n" + "-"*80)
    print("Ejecución completada")
    print("-"*80 + "\n")
    time.sleep(2)  # Pausa entre ejecuciones

# Lista de scripts a ejecutar
scripts = [
    ("base.py", "Ejemplo básico con un modelo de lenguaje"),
    ("temp.py", "Prueba de diferentes temperaturas en las respuestas"),
    ("systemPromt.py", "Uso de mensajes del sistema para controlar la salida"),
    ("keto_classification.py", "Clasificación de listas de compras como keto o no keto"),
    ("few_shot_prompting.py", "Prompting con ejemplos para clasificación de correos"),
    ("few_shot_lista_de_compras.py", "Conversión de unidades en listas de compras"),
    ("fechas_format.py", "Formateo de fechas en texto a formato YYYY/M/D"),
    ("factura_extractor.py", "Extracción estructurada de información de facturas"),
    ("clasificacion_sentimientos.py", "Análisis de sentimientos en tweets"),
    ("chain_of_thought_example.py", "Resolución de problemas matemáticos paso a paso")
]

if __name__ == "__main__":
    print("\n🚀 Iniciando ejecución de ejemplos de LangChain y OpenAI 🚀\n")
    
    for script_path, description in scripts:
        run_script(script_path, description)
    
    print("\n✅ Todos los ejemplos han sido ejecutados exitosamente ✅\n")
