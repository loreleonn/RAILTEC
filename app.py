# app.py
# Aplicación principal de validación normativa
# Proyecto RAILTEC – NAS 811

from reglas import (
    comprobar_tipo_senal,
    comprobar_distancia_senal_aguja,
    comprobar_longitud_circuito_via,
    comprobar_zona_muerta,
    comprobar_distancia_senal_baliza,
    comprobar_radio_curva
)


def main():
    print("========================================")
    print(" RAILTEC – VALIDACIÓN AUTOMÁTICA NAS 811 ")
    print("========================================\n")


    tipo_linea = input("Tipo de línea (Convencional / AV): ")
    tipo_via = input("Tipo de vía (general / apartado): ")
    tipo_senal = input("Tipo de señal (alta / baja): ")

    distancia_senal_aguja = float(
        input("Distancia señal – aguja (m): ")
    )

    longitud_cv = float(
        input("Longitud del circuito de vía (m): ")
    )

    zona_muerta = float(
        input("Longitud de la zona muerta entre CV (m): ")
    )

    sistema = input("Sistema de protección (ASFA / ERTMS): ")

    distancia_senal_baliza = float(
        input("Distancia señal – baliza (m): ")
    )

    velocidad = float(
        input("Velocidad máxima de la línea (km/h): ")
    )

    radio_curva = float(
        input("Radio de curva (m): ")
    )

  

    resultados = []

    r1 = comprobar_tipo_senal(tipo_linea, tipo_via, tipo_senal)
    resultados.append(("Tipo de señal (NAS 811)", r1))

    r2 = comprobar_distancia_senal_aguja(distancia_senal_aguja, tipo_linea)
    resultados.append(("Distancia señal‑aguja (NAS 811)", r2))

    r3 = comprobar_longitud_circuito_via(longitud_cv)
    resultados.append(("Longitud circuito de vía (NAS 811)", r3))

    r4 = comprobar_zona_muerta(zona_muerta)
    resultados.append(("Zona muerta entre CV (NAS 811)", r4))

    r5 = comprobar_distancia_senal_baliza(distancia_senal_baliza, sistema)
    resultados.append(("Distancia señal‑baliza (NAS 811)", r5))

    r6 = comprobar_radio_curva(radio_curva, velocidad)
    resultados.append(("Radio de curva", r6))


    print("\n----------------------------------------")
    print(" INFORME DE CUMPLIMIENTO NORMATIVO ")
    print("----------------------------------------\n")

    cumple_total = True

    for nombre, resultado in resultados:
        cumple, mensaje = resultado
        estado = "✅ CUMPLE" if cumple else "❌ NO CUMPLE"
        print(f"{nombre}: {estado}")
        print(f"  → {mensaje}\n")

        if not cumple:
            cumple_total = False

    print("----------------------------------------")
    if cumple_total:
        print("✅ CONCLUSIÓN FINAL: EL DISEÑO CUMPLE NAS 811")
    else:
        print("❌ CONCLUSIÓN FINAL: EL DISEÑO NO CUMPLE NAS 811")
    print("----------------------------------------")


if __name__ == "__main__":
    main()
