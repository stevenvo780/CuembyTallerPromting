import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

OPENROUTER_API_KEY = "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"
openai.api_key = OPENROUTER_API_KEY

# Factor de conversión preciso
KG_TO_LBS = 2.20462

def get_model(model_name="openai/gpt-4o-mini", openai_api_key=OPENROUTER_API_KEY, openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                      openai_api_key=openai_api_key,
                      openai_api_base=openai_api_base)

gpt4o = get_model()

few_shot_lista = f"""
Instrucciones: Convierte los pesos de la lista de compras de kilogramos (kg) a libras (lbs).
El factor de conversión es: 1 kg = {KG_TO_LBS} lbs. Redondea a 2 decimales.

Ejemplos:
Lista de compras: "Manzana: 1 kg"
Respuesta: "Apple: 2.20 lbs"

Lista de compras: "Zanahoria: 0.5 kg"
Respuesta: "Carrot: 1.10 lbs"

Lista de compras: "Tomate: 1.2 kg"
Respuesta: "Tomato: 2.65 lbs"

Ahora, procesa la siguiente lista de compras:
Aguacate: 1 kg
Pechuga de pollo: 1.5 kg
Salmón fresco: 1 kg
Huevos: 1 kg (~16 huevos medianos)
Brócoli: 0.5 kg
Espinacas frescas: 0.5 kg
Queso maduro (tipo manchego): 0.5 kg
Aceite de oliva extra virgen: 1 kg (aprox. 1 litro)
"""

message = HumanMessage(content=few_shot_lista)
result = gpt4o.invoke([message])
print("Respuesta:", result.content.strip())