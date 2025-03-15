#!/usr/bin/env python3
import sys
import subprocess

def main():
    # Obtener el modo de la línea de comandos, por defecto 'api'
    mode = sys.argv[1] if len(sys.argv) > 1 else "api"
    
    if mode == "api":
        print("🚀 Iniciando en modo API...")
        import api_service
        api_service.app.run(host='0.0.0.0', port=5000, debug=True)
    elif mode == "batch":
        print("🚀 Iniciando en modo ejecución secuencial...")
        import run_examples
    else:
        print("❌ Modo no reconocido. Opciones válidas: 'api' o 'batch'")
        sys.exit(1)

if __name__ == "__main__":
    main()
