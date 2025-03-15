from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini",openai_api_key:str=OPENROUTER_API_KEY, openai_api_base:str="https://openrouter.ai/api/v1" ) ->ChatOpenAI:
    return ChatOpenAI(model=model_name,
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base)

from formatter import format_response

gpt4o = get_model()

h1 = HumanMessage("Eres un psicologo que habla como emojis con falacias. ¿vale?")
result = gpt4o.invoke([h1])

print("Respuesta 1:")
print(format_response(result))
print("\n-------------------------\n")

h2 = HumanMessage("¿Qué es el amor?")
result2 = gpt4o.invoke([h1, result,h2])

print("Respuesta 2:")
print(format_response(result2))
