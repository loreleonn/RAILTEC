def generar_informe(resultados):

    texto = ""

    cumple_total = True

    for nombre, cumple, mensaje in resultados:

        estado = "✔ SI CUMPLE" if cumple else "✖ NO CUMPLE"

        texto += f"""
        <div style="
            background:#1e293b;
            padding:15px;
            border-radius:12px;
            margin-bottom:10px;
        ">

            <h3>{nombre}</h3>

            <p style="
                color:{'#22c55e' if cumple else '#ef4444'};
                font-weight:bold;
            ">
                {estado}
            </p>

            <p>{mensaje}</p>

        </div>
        """

        if not cumple:
            cumple_total = False

    if cumple_total:

        texto += """
        <h1 style='color:#22c55e'>
        ✔ EL DISEÑO CUMPLE NAS 811
        </h1>
        """

    else:

        texto += """
        <h1 style='color:#ef4444'>
        ✖ EXISTEN INCUMPLIMIENTOS
        </h1>
        """

    return texto