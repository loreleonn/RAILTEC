def generar_informe(resultados):
    print("Cumplimiento de la normatia segun los datos introducidos:\n")

    cumple_total = True

    for nombre, cumple, mensaje in resultados:
        estado = "SI CUMPLE" if cumple else "NO CUMPLE"
        print(f"{nombre}: {estado}")
        print(f"  → {mensaje}\n")

        if not cumple:
            cumple_total = False

    if cumple_total:
        print("EL DISEÑO CUMPLE COMPLETAMENTE CON LAS NORMAS NAS 811")
    else:
        print("EXISTEN INCUMPLIMIENTOS. ")
