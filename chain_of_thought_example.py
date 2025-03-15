from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import openai

OPENROUTER_API_KEY = "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"
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-3.5-turbo-0613", openai_api_key=OPENROUTER_API_KEY, 
              openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                      openai_api_key=openai_api_key,
                      openai_api_base=openai_api_base,
                      temperature=0)  # Agregamos temperatura 0 para resultados más deterministas

gpt4o = get_model()

sistema = SystemMessage(content="""
Eres un matemático meticuloso especializado en cálculos precisos.

INSTRUCCIONES DETALLADAS:
1. Para multiplicaciones largas, usa el método tradicional de multiplicación por columnas.
2. Descompón el cálculo en múltiples pasos pequeños. Muestra CADA paso intermedio.
3. Usa notación clara con números alineados correctamente.
4. Realiza verificaciones cruzadas para validar tu resultado:
   - Multiplica cada cifra individuamente y suma los resultados parciales
   - Verifica las unidades del resultado final para detectar errores de cálculo
5. Si el resultado parece incorrecto, vuelve a realizar todo el cálculo desde el principio.
6. NO REDONDEES ni aproximes ningún valor en ningún momento.

EJEMPLO DE MULTIPLICACIÓN LARGA:
Para multiplicar 123 × 45:
Paso 1: Multiplico 123 × 5
   123
 ×   5
 -----
   615  (5×3=15, escribo 5 y llevo 1; 5×2+1=11, escribo 1 y llevo 1; 5×1+1=6)

Paso 2: Multiplico 123 × 40
   123
 ×  40
 -----
  4920  (4×0=0; 4×3=12, escribo 2 y llevo 1; 4×2+1=9; 4×1=4)

Paso 3: Sumo los productos parciales
    615
   4920
   -----
   5535  (Resultado final: 123 × 45 = 5,535)

Verificación: 5×3=15, 5×2=10, 5×1=5, 4×3=12, 4×2=8, 4×1=4 → 15+10+50+120+80+400 = 5,535 ✓
""".strip())

humano = HumanMessage(content="""
Realiza meticulosamente esta multiplicación:

¿Cuánto es 4349 * 4434?

IMPORTANTE: 
1. Muestra TODOS los pasos intermedios 
2. Verifica tu resultado final con varios métodos
3. Asegúrate que el resultado es EXACTO sin aproximaciones
4. Si encuentras errores, vuelve a calcular desde el principio
""".strip())

resultado = gpt4o.invoke([sistema, humano])
print("Respuesta con cadena de razonamiento:\n", resultado.content.strip())

# Opcionalmente, podemos añadir un código para verificar el resultado
print("\nVerificación del resultado correcto:")
resultado_correcto = 4349 * 4434
print(f"4349 * 4434 = {resultado_correcto}")