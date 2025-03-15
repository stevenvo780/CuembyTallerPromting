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

gpt4o = get_model()

h1 = HumanMessage("Eres un psicologo que habla como emojis con falacias. ¿vale?")
result = gpt4o.invoke([h1])

print(result)

h2 = HumanMessage("¿Qué es el amor?")
result2 = gpt4o.invoke([h1, result,h2])

print(result2)
