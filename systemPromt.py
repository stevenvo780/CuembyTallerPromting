from langchain_openai import ChatOpenAI # Importar modulo para habilitar chat con OpenAI, pero usaremos openrouter
from langchain_core.messages import SystemMessage, HumanMessage
import os # para obtener variables de entorno
import openai  # Añadido

OPENROUTER_API_KEY = "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"
openai.api_key = OPENROUTER_API_KEY  # Añadido

def get_model(model_name="openai/gpt-4o-mini",openai_api_key:str=OPENROUTER_API_KEY, openai_api_base:str="https://openrouter.ai/api/v1" ) ->ChatOpenAI:
    # alternatively you can use OpenAI directly via ChatOpenAI(model="gpt-4o") via -> from langchain_openai import ChatOpenAI
    return ChatOpenAI(model=model_name,
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base)

# Cambio: Importar el servicio para formatear respuestas
from formatter import format_response

gpt4o = get_model()

s1 = SystemMessage(content="""
Clasifica como spam o no spam.
""")

h1 = HumanMessage("Hola, Ganaste un premio de 1000 dolares, solo debes hacer click en el siguiente enlace para reclamarlo.")

result = gpt4o.invoke([s1,h1])
print(result.content)