# basado en NAS 811 pricipalmete 



def comprobar_tipo_senal(tipo_linea, tipo_via, tipo_senal):
    tipo_linea = tipo_linea.lower()
    tipo_via = tipo_via.lower()
    tipo_senal = tipo_senal.lower()

    if tipo_linea == "av":
        if tipo_senal == "alta":
            return True, "Señal alta correcta en línea AV"
        return False, "En alta velocidad las señales deben ser altas"

    if tipo_linea == "convencional":
        if tipo_via == "general" and tipo_senal == "alta":
            return True, "Señal alta correcta en vía general"
        if tipo_via == "apartado" and tipo_senal == "baja":
            return True, "Señal baja correcta en vía de apartado"
        return False, "Tipo de señal incorrecto para la vía"

    return False, "Tipo de línea no reconocido"


def comprobar_distancia_senal_aguja(distancia, tipo_linea):
    tipo_linea = tipo_linea.lower()

    if tipo_linea == "convencional":
        return (
            distancia >= 200,
            "Distancia señal‑aguja correcta (≥ 200 m)" if distancia >= 200
            else "Distancia señal‑aguja insuficiente (≥ 200 m)"
        )

    if tipo_linea == "av":
        return (
            distancia >= 300,
            "Distancia señal‑aguja correcta (≥ 300 m)" if distancia >= 300
            else "Distancia señal‑aguja insuficiente (≥ 300 m)"
        )

    return False, "Tipo de línea no válido"



# regla de circuitos de via nas 811
def comprobar_circuito_via(longitud_cv, zona_muerta):
    mensajes = []
    cumple = True

    if longitud_cv < 20:
        cumple = False
        mensajes.append("Circuito de vía menor de 20 m")
    elif longitud_cv > 1200:
        cumple = False
        mensajes.append("Longitud de circuito de vía excesiva (≤ 1200 m)")
    else:
        mensajes.append("Longitud de circuito de vía correcta")

    if zona_muerta > 10:
        cumple = False
        mensajes.append("Zona muerta excesiva (≤ 10 m)")
    else:
        mensajes.append("Zona muerta dentro de límites")

    return cumple, "; ".join(mensajes)




#reglas de balizas nas 811, nas 154, nas 840
def comprobar_baliza(distancia, sistema):
    sistema = sistema.upper()

    if sistema == "ASFA":
        if distancia < 5:
            return False, "Baliza ASFA demasiado cercana a la señal"
        if distancia > 300:
            return False, "Baliza ASFA demasiado lejana (≤ 300 m)"
        return True, "Baliza ASFA correctamente situada"

    if sistema == "ERTMS":
        if distancia < 9:
            return False, "Baliza ERTMS demasiado cercana a la señal"
        if distancia > 1000:
            return False, "Baliza ERTMS demasiado lejana (≤ 1000 m)"
        return True, "Baliza ERTMS correctamente situada"

    return False, "Sistema de protección no reconocido"

#regla de trazado de memotria de via 
#geometría de la via, de que el radio de curva, pendiente y demas que sean compatibles

def comprobar_tramo_trazado(pk_inicio, pk_fin, radio, pendiente):
    cumple = True
    mensajes = []

    if radio < 1000:
        cumple = False
        mensajes.append("Radio de curva reducido para señalización")

    if abs(pendiente) > 25:
        cumple = False
        mensajes.append("Pendiente elevada (>25‰)")

    if cumple:
        mensajes.append("Tramo geométricamente compatible")

    return cumple, f"PK {pk_inicio} – {pk_fin}: " + "; ".join(mensajes)