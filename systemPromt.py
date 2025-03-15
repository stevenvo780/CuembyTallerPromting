import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI # Importar modulo para habilitar chat con OpenAI, pero usaremos openrouter
from langchain_core.messages import SystemMessage, HumanMessage
import openai 

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openai.api_key = OPENROUTER_API_KEY 

def get_model(model_name="openai/gpt-4o-mini",openai_api_key:str=OPENROUTER_API_KEY, openai_api_base:str="https://openrouter.ai/api/v1" ) ->ChatOpenAI:
    return ChatOpenAI(model=model_name,
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base)

from formatter import format_response

gpt4o = get_model()

s1 = SystemMessage(content="""
Clasifica como spam o no spam.
""")

h1 = HumanMessage("Hola, Ganaste un premio de 1000 dolares, solo debes hacer click en el siguiente enlace para reclamarlo.")

result = gpt4o.invoke([s1,h1])
print(result.content)