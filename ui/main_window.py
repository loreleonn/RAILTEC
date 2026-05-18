from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QComboBox, QLineEdit,
    QFrame, QScrollArea
)

from reglas import (
    comprobar_tipo_senal,
    comprobar_distancia_senal_aguja,
    comprobar_circuito_via,
    comprobar_baliza
)

from ui.styles import STYLE


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VALIDADOR ADIF · NAS 811")
        self.resize(1700, 900)
        self.setStyleSheet(STYLE)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(28)

        # ================= LEFT PANEL =================
        left = QFrame()
        left.setObjectName("panelCard")
        left_layout = QVBoxLayout(left)
        left_layout.setSpacing(24)
        left_layout.setContentsMargins(32, 32, 32, 32)

        titulo = QLabel("Parámetros de entrada")
        titulo.setObjectName("sectionTitle")

        subtitulo = QLabel("Introduce los datos de la instalación a validar")
        subtitulo.setObjectName("sectionSubtitle")

        left_layout.addWidget(titulo)
        left_layout.addWidget(subtitulo)

        # ✅ GRID CORRECTO EN 2 COLUMNAS
        form_grid = QGridLayout()
        form_grid.setHorizontalSpacing(24)
        form_grid.setVerticalSpacing(16)

        self.tipo_linea = QComboBox()
        self.tipo_linea.addItems(["Convencional", "AV"])

        self.tipo_via = QComboBox()
        self.tipo_via.addItems(["general", "apartado"])

        self.tipo_senal = QComboBox()
        self.tipo_senal.addItems(["alta", "baja"])

        self.sistema = QComboBox()
        self.sistema.addItems(["ASFA", "ERTMS"])

        self.distancia_senal = QLineEdit()
        self.distancia_senal.setPlaceholderText("m")

        self.distancia_baliza = QLineEdit()
        self.distancia_baliza.setPlaceholderText("m")

        self.longitud_cv = QLineEdit()
        self.longitud_cv.setPlaceholderText("m")

        self.zona_muerta = QLineEdit()
        self.zona_muerta.setPlaceholderText("m")

        campos = [
            ("Tipo de línea", self.tipo_linea),
            ("Tipo de vía", self.tipo_via),
            ("Tipo de señal", self.tipo_senal),
            ("Sistema", self.sistema),
            ("Distancia señal-aguja (m)", self.distancia_senal),
            ("Distancia de baliza (m)", self.distancia_baliza),
            ("Longitud circuito vía (m)", self.longitud_cv),
            ("Zona muerta (m)", self.zona_muerta),
        ]

        row = 0
        for i in range(0, len(campos), 2):

            # izquierda
            l1 = QLabel(campos[i][0])
            l1.setObjectName("fieldLabel")
            form_grid.addWidget(l1, row, 0)
            form_grid.addWidget(campos[i][1], row + 1, 0)

            # derecha
            l2 = QLabel(campos[i + 1][0])
            l2.setObjectName("fieldLabel")
            form_grid.addWidget(l2, row, 1)
            form_grid.addWidget(campos[i + 1][1], row + 1, 1)

            row += 2

        left_layout.addLayout(form_grid)

        self.btn_validar = QPushButton("Validar cumplimiento")
        self.btn_validar.setObjectName("validateButton")
        self.btn_validar.clicked.connect(self.validar)
        left_layout.addWidget(self.btn_validar)

        left_layout.addStretch()

        # ================= RIGHT PANEL =================
        right = QFrame()
        right.setObjectName("panelCard")
        right_layout = QVBoxLayout(right)
        right_layout.setSpacing(24)
        right_layout.setContentsMargins(32, 32, 32, 32)

        titulo2 = QLabel("Resultado de la validación")
        titulo2.setObjectName("sectionTitle")

        subtitulo2 = QLabel("Comprobación contra umbrales NAS 811")
        subtitulo2.setObjectName("sectionSubtitle")

        right_layout.addWidget(titulo2)
        right_layout.addWidget(subtitulo2)

        # ✅ SUMMARY CARD CORREGIDA
        self.summary_card = QFrame()
        self.summary_card.setObjectName("summaryCard")

        summary_layout = QHBoxLayout(self.summary_card)
        summary_layout.setContentsMargins(14, 12, 14, 12)
        summary_layout.setSpacing(12)

        self.summary_icon = QLabel("✔")
        self.summary_icon.setObjectName("summaryIcon")
        self.summary_icon.setFixedSize(28, 28)
        self.summary_icon.setAlignment(Qt.AlignCenter)

        text_container = QVBoxLayout()
        self.summary_status = QLabel("CUMPLE la normativa")
        self.summary_status.setObjectName("summaryStatus")

        self.summary_info = QLabel("ADIF NAS 811")
        self.summary_info.setObjectName("summaryInfo")

        text_container.addWidget(self.summary_status)
        text_container.addWidget(self.summary_info)

        summary_layout.addWidget(self.summary_icon)
        summary_layout.addLayout(text_container)

        right_layout.addWidget(self.summary_card)

        # RESULTADOS
        self.results_list_widget = QWidget()
        self.results_list_layout = QVBoxLayout(self.results_list_widget)
        self.results_list_layout.setSpacing(0)
        self.results_list_layout.setContentsMargins(0, 0, 0, 0)

        right_layout.addWidget(self.results_list_widget)

        note_text = QLabel(
            "Umbrales orientativos según ADIF NAS 811. Verifica siempre con la edición vigente."
        )
        note_text.setObjectName("noteText")
        note_text.setWordWrap(True)

        right_layout.addWidget(note_text)

        right_layout.addStretch()

        layout.addWidget(left, 2)
        layout.addWidget(right, 3)

        self.setLayout(layout)

        self.mostrar_resultados([])

    # ================= RESULTADOS =================

    def mostrar_resultados(self, resultados):
        for i in reversed(range(self.results_list_layout.count())):
            item = self.results_list_layout.takeAt(i)
            if item.widget():
                item.widget().deleteLater()

        cumple_total = True

        for nombre, cumple, mensaje in resultados:
            card = QFrame()
            card.setObjectName("resultCard")

            card_layout = QHBoxLayout(card)
            card_layout.setContentsMargins(0, 12, 0, 12)
            card_layout.setSpacing(12)

            text_layout = QVBoxLayout()
            text_layout.setSpacing(4)

            titulo = QLabel(nombre)
            titulo.setObjectName("resultTitle")

            desc = QLabel(mensaje)
            desc.setObjectName("resultSubtitle")
            desc.setWordWrap(True)

            text_layout.addWidget(titulo)
            text_layout.addWidget(desc)

            badge = QLabel("OK" if cumple else "FALLO")
            badge.setObjectName("resultBadge")
            badge.setProperty("estado", "ok" if cumple else "fail")
            badge.setAlignment(Qt.AlignCenter)
            badge.setFixedSize(75, 32)

            card_layout.addLayout(text_layout)
            card_layout.addStretch()
            card_layout.addWidget(badge)

            self.results_list_layout.addWidget(card)

            if not cumple:
                cumple_total = False

        if resultados:
            if cumple_total:
                self.summary_status.setText("CUMPLE la normativa")
                self.summary_icon.setText("")
                self.summary_card.setProperty("estado", "ok")
            else:
                self.summary_status.setText("NO CUMPLE la normativa")
                self.summary_icon.setText("")
                self.summary_card.setProperty("estado", "fail")
        else:
            self.summary_status.setText("Aún no se han validado datos")
            self.summary_icon.setText("")
            self.summary_card.setProperty("estado", "info")
            self.summary_info.setText("Complete el formulario y presione validar.")

        self.summary_card.style().unpolish(self.summary_card)
        self.summary_card.style().polish(self.summary_card)

    # ================= VALIDACIÓN =================

    def validar(self):
        try:
            resultados = []

            r1 = comprobar_tipo_senal(
                self.tipo_linea.currentText(),
                self.tipo_via.currentText(),
                self.tipo_senal.currentText()
            )
            resultados.append(("Tipo señal", r1[0], r1[1]))

            r2 = comprobar_distancia_senal_aguja(
                float(self.distancia_senal.text()),
                self.tipo_linea.currentText()
            )
            resultados.append(("Distancia señal-aguja", r2[0], r2[1]))

            r3 = comprobar_circuito_via(
                float(self.longitud_cv.text()),
                float(self.zona_muerta.text())
            )
            resultados.append(("Circuito de vía", r3[0], r3[1]))

            r4 = comprobar_baliza(
                float(self.distancia_baliza.text()),
                self.sistema.currentText()
            )
            resultados.append(("Balizamiento", r4[0], r4[1]))

            self.mostrar_resultados(resultados)

        except Exception as e:
            self.mostrar_resultados([])