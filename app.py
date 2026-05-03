from reglas import (
    comprobar_tipo_senal,
    comprobar_distancia_senal_aguja,
    comprobar_circuito_via,
    comprobar_baliza,
    comprobar_tramo_trazado
)

from informe import generar_informe


def main():
    print("VALIDACIÓN DE DISEÑO DE VÍA (segun la normativa establecida por ADIF) ")

    # datos de entrada generales para la validación 
    tipo_linea = input("Tipo de línea (Convencional / AV): ")
    tipo_via = input("Tipo de vía (general / apartado): ")
    tipo_senal = input("Tipo de señal (alta / baja): ")
    distancia_senal_aguja = float(input("Distancia señal‑aguja (m): "))
    sistema = input("Sistema (ASFA / ERTMS): ")
    distancia_baliza = float(input("Distancia señal‑baliza (m): "))

    # circuitos de la via 
    print("\nCIRCUITOS DE VÍA:")
    longitud_cv = float(input("Longitud del circuito de vía (m): "))
    zona_muerta = float(input("Zona muerta entre circuitos (m): "))

    # tamos que van a ser validados 
    print("\nTRAMOS DE TRAZADO:")
    num_tramos = int(input("Número de tramos a validar (máximo 5): "))
    
    if num_tramos < 1 or num_tramos > 5:
        print("\n el numero de tramos a validar debe estar entre 1 y 5.")
        return

    resultados = []

    # relgas generales de la normativa adif 
    r1 = comprobar_tipo_senal(tipo_linea, tipo_via, tipo_senal)
    resultados.append(("Tipo de señal (NAS 811)", r1[0], r1[1]))

    r2 = comprobar_distancia_senal_aguja(distancia_senal_aguja, tipo_linea)
    resultados.append(("Distancia señal‑aguja (NAS 811)", r2[0], r2[1]))

    r3 = comprobar_circuito_via(longitud_cv, zona_muerta)
    resultados.append(("Circuitos de vía (NAS 811)", r3[0], r3[1]))

    r4 = comprobar_baliza(distancia_baliza, sistema)
    resultados.append(("Balizamiento (NAS 811)", r4[0], r4[1]))

    # Reglas por tramo
    for i in range(num_tramos):
        print(f"\nTramo {i + 1}")
        pk_ini = input("PK inicio: ")
        pk_fin = input("PK fin: ")
        radio = float(input("Radio de curva (m): "))
        pendiente = float(input("Pendiente (‰): "))

        cumple, mensaje = comprobar_tramo_trazado(
            pk_ini, pk_fin, radio, pendiente
        )
        resultados.append((f"Tramo {pk_ini}–{pk_fin}", cumple, mensaje))

    # devuelve al final de que si cumple o no, cuales si y cuales no 
    generar_informe(resultados)


if __name__ == "__main__":
    main()