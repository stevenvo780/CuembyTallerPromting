import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

OPENROUTER_API_KEY = "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"
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini", openai_api_key=OPENROUTER_API_KEY, openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                      openai_api_key=openai_api_key,
                      openai_api_base=openai_api_base)

gpt4o = get_model()

few_shot_keto = """
Ejemplos:
Lista de compras: "Pechuga de pollo, espárragos, aceite de oliva"
Clasificación: Keto

Lista de compras: "Pan de caja, refresco, galletas"
Clasificación: No Keto

Lista de compras: "Ensalada de espinacas, aguacate, aceite de oliva"
Clasificación: Keto

Lista de compras: "Cereal, leche entera, galletas de chocolate"
Clasificación: No Keto

Lista de compras: "Filete de salmón, aguacate, col rizada"
Clasificación: Keto

Lista de compras: "Pan integral, fresas, yogur con azúcar"
Clasificación: No Keto

Ahora, clasifica sintéticamente las siguientes listas de compras:
1) Aguacate, huevos, mantequilla, espinacas, salmón, queso cheddar.
2) Pechuga de pollo, brócoli, crema de coco, tocino, almendras, aceite de oliva.
3) Atún enlatado, coliflor, mantequilla de almendra, calabacín, carne molida de res, chocolate negro (85%+).
4) Jamón serrano, nuez pecana, espárragos, crema para batir, champiñones, aceitunas verdes.
5) Queso de cabra, chicharrón, apio, sardinas enlatadas, yogur griego sin azúcar, semillas de chía.
6) Pan de caja, plátanos, arroz blanco, frijoles negros, leche de vaca, galletas dulces.
7) Pasta, salsa de tomate, papas, manzanas, yogur de sabores, miel.
8) Cereal de desayuno, azúcar blanca, jugo de naranja, harina de trigo, mermelada, pan dulce.
9) Nachos, refresco, chocolate con leche, helado, croissants, papas fritas.
10) Tortillas de maíz, arroz integral, zanahorias, lentejas, queso crema con azúcar, dátiles.
"""

message = HumanMessage(content=few_shot_keto)
result = gpt4o.invoke([message])
print("Clasificación:", result.content.strip())