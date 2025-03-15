from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
import openai 

OPENROUTER_API_KEY = "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"
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini",openai_api_key:str=OPENROUTER_API_KEY, openai_api_base:str="https://openrouter.ai/api/v1" ) ->ChatOpenAI:
    return ChatOpenAI(model=model_name,
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base)

from formatter import format_response

gpt4o = get_model()

temp = [0, 0.3, 0.5, 0.7, 0.9, 1.0, 2.0]
h1 = HumanMessage("¿Qué consejos le darías a alguien que viaja en el tiempo desde hace 200 años hacia la actualidad?")
responses = []
for t in temp:
    print(f"Temperatura: {t}")
    result = gpt4o.invoke([h1], temperature=t)
    print(format_response(result))
    print("--" * 10)
    responses.append(format_response(result))