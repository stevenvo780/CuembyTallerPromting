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

few_shot1 = """Correo: "Oferta limitada: gana dinero fácil desde casa."
Clasificación: spam.

Correo: "Factura de electricidad disponible para consulta."
Clasificación: legítimo.

Correo: "Felicitaciones, has ganado un premio increíble."
Clasificación: spam.

Correo: "Resumen de la reunión del día lunes."
Clasificación:"""

h1 = HumanMessage(content=few_shot1)
result = gpt4o.invoke([h1])
print("Clasificación:", result.content.strip())