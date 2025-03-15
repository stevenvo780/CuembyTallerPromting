import os
from dotenv import load_dotenv
load_dotenv()

import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini", openai_api_key=OPENROUTER_API_KEY, openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                      openai_api_key=openai_api_key,
                      openai_api_base=openai_api_base)

gpt4o = get_model()

few_shot_fechas = """
Ejemplos:
Texto: "La reunión es el 5 de abril de 2020."
Respuesta: "2020/4/5"

Texto: "La fiesta fue el 30 de noviembre de 2019."
Respuesta: "2019/11/30"

Texto: "El evento ocurrirá el 1 de enero de 2022."
Respuesta: "2022/1/1"

Texto: "El taller se realizará el 22 de julio de 2018."
Respuesta: "2018/7/22"

Texto: "La sesión fue el 9 de diciembre de 2017."
Respuesta: "2017/12/9"

Ahora, procesa los siguientes textos y retorna únicamente las fechas encontradas en formato YYYY/M/D:
1) "La conferencia fue el 15 de mayo en Barcelona. Hoy es 01 de septiembre del 2001"
2) "La boda de Carlos y Ana será el 12 de junio en Madrid de este año."
3) "El concierto de Shakira que era el 20 de febrero lo cancelaron, lo van a reprogramar en otra fecha del 2025"
"""
message = HumanMessage(content=few_shot_fechas)
result = gpt4o.invoke([message], temperature=0.2)
print("Respuesta: \n")
print(result.content.strip())