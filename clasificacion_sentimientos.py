import os
from dotenv import load_dotenv
load_dotenv()

import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini", openai_api_key=OPENROUTER_API_KEY, openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                      openai_api_key=openai_api_key,
                      openai_api_base=openai_api_base)

# Definición de tweets
trino1 = """
Otra vez llegué tarde al trabajo por el pésimo servicio del transporte público. ¡Estoy harto!
""" # negativo
trino2 = """
Qué decepción la película, esperaba mucho más después de tanto ruido. Una pérdida de tiempo.
""" # negativo
trino3 = """
¡Hoy recibí la mejor noticia! Por fin conseguí ese trabajo que tanto quería. ¡Estoy feliz!
""" # positivo
trino4 = """
La reunión mensual con el equipo será mañana a las 10:00 am, en la sala principal.
""" # neutro

tweets = [trino1, trino2, trino3, trino4]

model = get_model()

print("Clasificación de Sentimientos:")
for idx, tweet in enumerate(tweets, start=1):
    sistema = SystemMessage(content="""
Instrucciones: Clasifica el sentimiento del siguiente tweet.
Contexto: El tweet proviene de redes sociales y puede expresar opiniones o hechos.
Rol: Actúa como un analista de sentimientos.
Formato: Responde únicamente con una palabra: 'positivo', 'negativo' o 'neutro'.
Tono: Formal y conciso.
Ejemplo: Si el tweet dice 'Me encanta este día', responde 'positivo'.
""")
    humano = HumanMessage(content=tweet)
    resultado = model.invoke([sistema, humano], temperature=0.2)
    print(f"Tweet {idx}: {resultado.content.strip()}")