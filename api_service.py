from flask import Flask, jsonify, request
import subprocess
import os
import sys
import time

app = Flask(__name__)

# Lista de ejercicios disponibles
exercises = [
    {"id": "base", "file": "base.py", "description": "Ejemplo básico con un modelo de lenguaje"},
    {"id": "temp", "file": "temp.py", "description": "Prueba de diferentes temperaturas en las respuestas"},
    {"id": "systemPromt", "file": "systemPromt.py", "description": "Uso de mensajes del sistema para controlar la salida"},
    {"id": "keto", "file": "keto_classification.py", "description": "Clasificación de listas de compras como keto o no keto"},
    {"id": "few_shot", "file": "few_shot_prompting.py", "description": "Prompting con ejemplos para clasificación de correos"},
    {"id": "lista_compras", "file": "few_shot_lista_de_compras.py", "description": "Conversión de unidades en listas de compras"},
    {"id": "fechas", "file": "fechas_format.py", "description": "Formateo de fechas en texto a formato YYYY/M/D"},
    {"id": "factura", "file": "factura_extractor.py", "description": "Extracción estructurada de información de facturas"},
    {"id": "sentimientos", "file": "clasificacion_sentimientos.py", "description": "Análisis de sentimientos en tweets"},
    {"id": "chain_thought", "file": "chain_of_thought_example.py", "description": "Resolución de problemas matemáticos paso a paso"}
]

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API de ejercicios LangChain y OpenAI",
        "endpoints": {
            "GET /api/exercises": "Listar todos los ejercicios disponibles",
            "POST /api/execute/<exercise_id>": "Ejecutar un ejercicio específico"
        }
    })

@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    """Endpoint para listar todos los ejercicios disponibles"""
    return jsonify({
        "status": "success",
        "exercises": exercises,
        "count": len(exercises)
    })

@app.route('/api/execute/<exercise_id>', methods=['POST'])
def execute_exercise(exercise_id):
    """Endpoint para ejecutar un ejercicio específico"""
    # Buscar el ejercicio por ID
    exercise = next((ex for ex in exercises if ex["id"] == exercise_id), None)
    
    if not exercise:
        return jsonify({
            "status": "error",
            "message": f"Ejercicio con ID '{exercise_id}' no encontrado"
        }), 404
    
    try:
        # Ejecutar el script como subprocess para capturar la salida
        result = subprocess.run(
            [sys.executable, exercise["file"]], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode != 0:
            return jsonify({
                "status": "error",
                "message": "Error al ejecutar el ejercicio",
                "stdout": result.stdout,
                "stderr": result.stderr
            }), 500
        
        return jsonify({
            "status": "success",
            "exercise": exercise,
            "output": result.stdout
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error al ejecutar el ejercicio: {str(e)}"
        }), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de ejercicios LangChain y OpenAI")
    print("📋 Endpoints disponibles:")
    print("   - GET /api/exercises: Listar todos los ejercicios")
    print("   - POST /api/execute/<exercise_id>: Ejecutar un ejercicio específico")
    app.run(host='0.0.0.0', port=5000, debug=True)
