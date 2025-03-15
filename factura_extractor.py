import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import openai
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openai.api_key = OPENROUTER_API_KEY

def get_model(model_name="openai/gpt-4o-mini", openai_api_key=OPENROUTER_API_KEY, openai_api_base="https://openrouter.ai/api/v1") -> ChatOpenAI:
    return ChatOpenAI(model=model_name,
                     openai_api_key=openai_api_key,
                     openai_api_base=openai_api_base)

factura001 = """
### Factura de Servicios Públicos EPM

**Encabezado:**
*   **Dirección prestación servicio:** calle falsa 123 (interior 301)
*   **Municipio:** Medellín - Antioquia

**Información General:**

*   **Documento Equivalente Electrónico SPD N°:** DEE100439
*   **Contrato:** 4071023
*   **Referente de pago:** 1058617580-22
*   **Documento No:** 12345
*   **Cliente:** Homero J Simpson
*   **CC/NIT:** 123456789
*   **Dirección de cobro:** calle falsa 123 (INTERIOR 301)
*   **Medellín - Antioquia**
*   **Estrato:** 3
*   **Ciclo:** 16
*   **Código de barras:** 0584100400001-16-001628151

*   **Valor total a pagar:** $449.970
*   **Pagar hasta el:** 11-mar-2025
*   El pago después de esta fecha generará intereses de mora.

**Imágenes:**
*   Código QR con información del contrato y valores.
*   Imagen de incremento/decremento/igual en los servicios.

---
#### Acueducto

*   **Cálculo Consumo del 04 ene al 04 feb (31 días)**
    *   Lectura actual: 1.774
    *   Lectura anterior: 1.748
    *   Consumo: 26 m³

    *   **Valores Facturados**
        *   Consumo feb-25: 13 m³ x 4.687,36 = $60.935,68
        *   Consumo feb-25: 13 m³ x 4.687,36 = $60.935,68
        *   Cargo fijo feb-25: 9.252,53
        *   Subsidio: -8.773,53
        *   Interés mora %0,4856 emv: 87,64
        *   **Total Acueducto:** $122.438
    *   **Observaciones:** 30 - variación nivel de utilización.
    *   **Información del producto:**
        *   Producto: 110679798
        *   Categoría: Residencial
        *   Medidor: water Tech_sirius_20 16609297-7
        *   Plan: Residencial
        *   Componentes del costo:
            *   Cmapac - Cost,00
            *   Cmpac Unitario 2,11
            *   Cmpac Total 54,86
            *   Cmt Unitario 26,78
            *   Cmt Total 696,28
    *   **Histórico de consumos (m³) y promedio**

    **Imagen:**
    *   Gráfico de histórico de consumos de acueducto.

---
#### Alcantarillado

*   **Cálculo Consumo del 04 ene al 04 feb (31 días)**
    *   Consumo: 26 m³

    *   **Valores Facturados**
        *   Consumo feb-25: 13 m³ x 3.587,61 = $46.638,93
        *   Consumo feb-25: 13 m³ x 3.587,61 = $46.638,93
        *   Cargo fijo feb-25: 5.321,40
        *   Subsidio: -6.495,05
        *   Interés mora %0,4856 emv: 65,82
        *   **Total Alcantarillado:** $92.170,03

    *   **Información del producto:**
        *   Producto: 110679105
        *   Categoría: Residencial
        *   Plan: Residencial
        *   Componentes del costo:
            *   Cmt Unitario 17,03
            *   Cmt Total 442,78
    *   **Histórico de consumos (m³) y promedio**

    **Imagen:**
        *   Gráfico de histórico de consumos de alcantarillado.

---
#### Energía

*   **Cálculo Consumo del 04 ene al 04 feb (31 días)**
    *   Lectura actual: 31.147
    *   Lectura anterior: 30.986
    *   Constante: 1
    *   Consumo: 161 kWh

    *   **Valores Facturados**
        *   Energía feb-25: 161 kWh x 913,53 = $147.078,33
        *   Subsidio: -17.813,84
        *   Interés mora %0,4856 emv: 91,82
        *   **Total Energía:** $129.356,31
    *   **Información del producto:**
        *   Producto: 110482866
        *   Categoría: Residencial
        *   Medidor: 46_oa3tci_2719957-3
        *   Plan: Normal residencial
        *   Componentes del costo:
            *   Generación 371,11
            *   Transmisión 56,03
            *   Distribución 292,11
            *   Comercializac 115,65
            *   Pérdidas 74,91
            *   Restricciones 3,71
        *   N. tensión: 220 voltios
    *   **Histórico de consumos (kWh) y promedio**

    **Imagen:**
        *   Gráfico de histórico de consumos de energía.

---
#### Gas

*   **Cálculo Consumo del 04 ene al 04 feb (31 días)**
    *   Lectura actual: 2.433
    *   Lectura anterior: 2.409
    *   Constante: 0,845
    *   Consumo: 20,287 m³

    *   **Valores Facturados**
        *   Consumo feb-25: 20,287 m³ x 2.946,73 = $59.780,31
        *   Cargo fijo feb-25: 4.065,40
        *   Interés mora %0,4856 emv: 34,15
        *   **Total Gas:** $63.879,86
    *   **Información del producto:**
        *   Producto: 120694646
        *   Categoría: Residencial
        *   Medidor: 78_g1.6(g1.6)_20136483401-9
        *   Plan: Residencial tarifa plena
        *   Componentes del costo:
            *   Componentes Variables: ($/m3)
                *   Compra 1.481,94
                *   Distribución 692,72
                *   Transporte 578,04
                *   Confiabilidad ,00
                *   Comercializac ,00
            *   Componentes Fijas ($/factura)
                *   Transporte Gn 161,70
                *   Compresión 32,31
                *   Comercializac 4.065,40
    *   **Histórico de consumos (m³) y promedio**
    **Imagen:**
        *   Gráfico de histórico de consumos de gas.

---
#### Ajuste conceptos facturados

*   Epm a tu puerta
    *   Detalles del producto
        *   Producto #132262268
        *   Descripción
            *   Asistencia epm a tu puerta
        *   Interés mora %0,4856 emv
        *   Interés mora x recaudo iva
*   Valores facturados
    *   Asistencia epm a tu puerta $ 10.840,34
    *   Interés mora $ 1,33
    *   Interés mora x recaudo iva $7,02

*   Servicio, Concepto-Periodo
    *   (Alcantarillado - Consumo Oct-24) Valor ($) 15,60
    *   (Alcantarillado - Subs Consumo Oct-24) Valor ($) -1,06
    *   Alcantarillado - Consumo Nov-24 Valor ($) 15,60
    *   Alcantarillado - Subs Consumo Nov-24 Valor ($) -1,06

*   **Total Ajuste conceptos facturados: $ 10.848,69**

---
#### Otras Entidades

*   **Emvarias:**

    *   Empresas Varias De Medellín E.s.p. Nit: 8909050559 Tel:6044445636 Email: contacto@emvarias.com.co Dir: cr 58 42-125 edif. inteligente Web: www.emvarias.com.co Producto: 110505343
    *   Usuario: Homero J Simpson - Residencial - Estrato 3 - calle falsa 123 (interior 301) - Medellín - Antioquia Frecuencias: Semanal No Aprovechables: 2 - Barrido: 2 Mensual Periodo de consumo: Diciembre 2024 Aforo: Pago periodo anterior:

    *   **Valores facturados**
        *   Cargo Fijo: $14.049,68
        *   Cargo Variable Aprovechable: $1.262,28
        *   Barrido y limpieza: $-4.208,69
        *   Limpieza urbana: $19,29
        *   Subsidio 15%:
        *   Interés Mora %0,4856 Emv:
        *   **Total Aseo:** $12.746,01
        *   Valor Servicio facturado (últimos 6 meses)
            *   Nov-24 $ 23.871,65
            *   Oct-24 $ 23.837,26
            *   Sep-24 $ 23.887,18
            *   Ago-24 $ 25.051,21
            *   Jul-24 $ 23.855,38
            *   Jun-24 $ 24.144,64
        *   Residuos del periodo (ton)
            *   No Aprov - Ordinarios 0,04357
        *   Cantidad de residuos (ton)
            *   Aprovechables No Aprovechables
                *   Rechazados 0,002 0,00019
                *   Dic-24 0,00005 0,04588
                *   Nov-24 0,00554 0,04588
                *   Oct-24 0,00508 0,04588
                *   Dic-24 0,00505
            *   Cargo Variable
        *   **Total Aseo:** $23.868,57

*   **Alumbrado Público:**

    *   Alumbrado Público Municipio De Medellín Nit: 8909052111 Tel: 604 4444144 Email: alumbradopublicomed@medellin.gov.co Dir: calle 44 #52-165 alcaldia medellin tesoreria piso 1 taquilla 6 Web: www.medellin.gov.co Producto: 126117983
    *   Usuario: Homero J Simpson - Residencial - Estrato 3 - calle falsa 123 (interior 301) - Medellín
    *   **Valores Facturados**
        *   Antioquia - Acuerdo 066 De 2017 - Ccu Cláusula 36 Parágrafo 3 Pago periodo anterior:
        *   Alumbrado Público: $ 5.300,00
        *   Interés Mora %0,4856 Emv: $ 4,29
        *   **Total Alumbrado:** $ 5.304,29

*   **Otros Cobros:**

    *   **Concepto:**
        *   Iva 19% Interés Mora X Reca: 1,33
        *   Iva Asistencia Epm A Tu Pue: 2.059,66

    *   **Total epm a tu puerta:** $2.060,99
    *   **Total Otras Entidades:** $31.233,85

---
**Información Adicional y Contacto:**

*   Estamos ahí más cerca de tí:
    *   Medellín (604) 4444115
    *   Resto del país 018000415115
*   Línea ética: "Contacto Transparente" 018000522955
*   Empresas Públicas de Medellín E.S.P NIT.890.904.996-1
*   Puntos de Pago: Paga en línea: APP-EPM
    *   https://aplicaciones.epm.com.co/facturaweb/#/
*   Direcciones y detalles de contacto para Puntos de Pago.
*   Información técnica
*   *Entidades que nos regulan Comision de Regulacion de Agua Potable y Saneamiento Basico CRA - www.cra.gov.co / Comision de Regulacion de Energia y Gas CREG - www.creg.gov.co*

**Información legal:**

*   *La presente factura presta mérito ejecutivo en virtud del artículo 130 de la Ley 142 de 1994 modificado por el artículo 18 de la Ley 689 de 2001.*

**Firmas:**
*   Representante legal
*   Gerente Empresas Varias de Medellín S.A E.S.P

**Imágenes:**

*   Logo de EPM
*   Logo de Emvarias
*   Logo Superservicios
x
---
"""

output_parser = """
Analiza la factura proporcionada y extrae la siguiente información en formato JSON:
1. nombre_cliente: El nombre completo del cliente
2. direccion_cobro: La dirección completa donde se envía la factura
3. estrato: El estrato socioeconómico del cliente (como número)
4. valor_total_energia: El valor total a pagar por el servicio de energía (como número sin símbolos de moneda)
5. costo_kilovatio_hora: El costo unitario por kilovatio hora (como número sin símbolos de moneda)

Responde exclusivamente con un objeto JSON válido que contenga estos 5 campos, sin explicaciones adicionales.
"""

gpt4o = get_model()
result = gpt4o.invoke([HumanMessage(content=factura001)])
result = gpt4o.invoke([SystemMessage(content=output_parser), result])

try:
    datos_factura = json.loads(result.content)
    print("Información extraída de la factura:")
    for key, value in datos_factura.items():
        print(f"{key}: {value}")
    
    print("\nObjeto JSON completo:")
    print(json.dumps(datos_factura, indent=2, ensure_ascii=False))
except json.JSONDecodeError:
    print("Error al decodificar la respuesta JSON.")
    print("Respuesta recibida:")
    print(result.content)
