# reglas.py
# Motor de reglas normativas ADIF
# Basado principalmente en NAS 811 (Edición 3)
# Proyecto RAILTEC – Validaciones Automáticas



# regla NAS - 811 

def comprobar_tipo_senal(tipo_linea, tipo_via, tipo_senal):
    """
    NAS 811 – 6.2 Señales

    Convencional:
      - Vía general → señal alta
      - Vía de apartado → señal baja
    Alta Velocidad:
      - Todas las señales deben ser altas
    """

    tipo_linea = tipo_linea.lower()
    tipo_via = tipo_via.lower()
    tipo_senal = tipo_senal.lower()

    if tipo_linea == "av":
        if tipo_senal == "alta":
            return True, "Cumple NAS 811: señal alta en línea de Alta Velocidad"
        else:
            return False, "No cumple NAS 811: en alta velocidad las señales deben ser altas"

    if tipo_linea == "convencional":
        if tipo_via == "general" and tipo_senal == "alta":
            return True, "Cumple NAS 811: señal alta en vía general"
        if tipo_via == "apartado" and tipo_senal == "baja":
            return True, "Cumple NAS 811: señal baja en vía de apartado"
        return False, "No cumple NAS 811: tipo de señal incorrecto para la vía"

    return False, "Datos de línea o vía no válidos"


def comprobar_distancia_senal_aguja(distancia, tipo_linea):
    """
    NAS 811 – 6.2
    Distancia mínima recomendada entre señal y punta de aguja
      - Convencional: ≥ 20 m
      - Alta Velocidad: ≥ 30 m
    """

    tipo_linea = tipo_linea.lower()

    if tipo_linea == "convencional" and distancia >= 20:
        return True, "Cumple NAS 811: distancia señal‑aguja adecuada en línea convencional"

    if tipo_linea == "av" and distancia >= 30:
        return True, "Cumple NAS 811: distancia señal‑aguja adecuada en alta velocidad"

    return False, "No cumple NAS 811: distancia señal‑aguja insuficiente"


def comprobar_longitud_circuito_via(longitud_cv):
    """
    NAS 811 – 6.3 Circuitos de vía
    Longitud mínima de un circuito de vía: 20 m
    """

    if longitud_cv >= 20:
        return True, "Cumple NAS 811: longitud mínima del circuito de vía"
    else:
        return False, "No cumple NAS 811: el circuito de vía es menor de 20 m"


def comprobar_zona_muerta(longitud_zm):
    """
    NAS 811 – 6.3
    Zona muerta entre circuitos de vía:
    Recomendable < 3 m
    """

    if longitud_zm <= 3:
        return True, "Cumple NAS 811: zona muerta dentro de límites"
    else:
        return False, "No cumple NAS 811: zona muerta excesiva entre CV"



def comprobar_distancia_senal_baliza(distancia, sistema):
    """
    NAS 811 / NAS 154 / NAS 840
    Distancia mínima señal – baliza de pie:
      - ASFA: ≥ 5 m
      - ERTMS: ≥ 9 m
    """

    sistema = sistema.upper()

    if sistema == "ASFA" and distancia >= 5:
        return True, "Cumple NAS 811: distancia señal‑baliza ASFA correcta"

    if sistema == "ERTMS" and distancia >= 9:
        return True, "Cumple NAS 811: distancia señal‑baliza ERTMS correcta"

    return False, "No cumple NAS 811: distancia señal‑baliza insuficiente"


def comprobar_radio_curva(radio, velocidad):
    """
    Regla geométrica simplificada compatible con criterios ADIF
    """

    if velocidad <= 160 and radio >= 1000:
        return True, "Radio de curva adecuado para la velocidad"
    elif velocidad > 160 and radio >= 2500:
        return True, "Radio de curva adecuado para alta velocidad"
    else:
        return False, "Radio de curva insuficiente para la velocidad establecida"
