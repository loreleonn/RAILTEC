STYLE = """

/* ================= BASE ================= */

QWidget {
    background-color: #e5e7eb;
    color: #111827;
    font-family: Segoe UI, sans-serif;
    font-size: 14px;
}

/* ================= PANEL PRINCIPAL ================= */

QFrame#panelCard {
    background-color: #ffffff;
    border-radius: 24px;
    border: 1px solid #e5e7eb;
    padding: 24px;
}

/* ================= TEXTOS ================= */

QLabel#sectionTitle {
    font-size: 22px;
    font-weight: 700;
    color: #111827;
}

QLabel#sectionSubtitle {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 12px;
}

QLabel#fieldLabel {
    font-size: 13px;
    color: #475569;
    margin-bottom: 6px;
}

/* ================= INPUTS ================= */

QLineEdit,
QComboBox {
    background-color: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 10px 14px;
    color: #111827;
    min-height: 36px;
}

QLineEdit:focus,
QComboBox:focus {
    border: 1px solid #2563eb;
    background-color: #ffffff;
}

/* ================= TABLA ================= */

QTableWidget {
    background-color: #ffffff;
    border: none;
    border-radius: 12px;
    gridline-color: transparent;
}

QHeaderView::section {
    background-color: transparent;
    color: #111827;
    padding: 10px;
    border: none;
    font-weight: 600;
}

QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #f1f5f9;
}

/* ================= BOTÓN ================= */

QPushButton#validateButton {
    background-color: #b91c1c;
    color: white;
    border-radius: 12px;
    padding: 14px;
    font-size: 14px;
    font-weight: 700;
}

QPushButton#validateButton:hover {
    background-color: #dc2626;
}

/* ================= SUMMARY CARD ================= */

QFrame#summaryCard {
    border-radius: 12px;
    padding: 10px 12px;
    background-color: #e0f2fe;
    border: 1px solid #bae6fd;
}

QFrame#summaryCard[estado='ok'] {
    background-color: #dcfce7;
    border: 1px solid #86efac;
}

QFrame#summaryCard[estado='fail'] {
    background-color: #fee2e2;
    border: 1px solid #fecaca;
}

QFrame#summaryCard[estado='info'] {
    background-color: #e0f2fe;
    border: 1px solid #7dd3fc;
}

/* ================= ICONO ================= */

QLabel#summaryIcon {
    font-size: 0px;
    min-width: 0px;
    min-height: 0px;
    background-color: transparent;
    color: transparent;
    border-radius: 0px;
    padding: 0px;
}

QFrame#summaryCard[estado='ok'] QLabel#summaryIcon {
    background-color: transparent;
}

QFrame#summaryCard[estado='info'] QLabel#summaryIcon {
    background-color: transparent;
}

/* ================= TEXTO SUMMARY ================= */

QLabel#summaryStatus {
    font-size: 16px;
    font-weight: 700;
}

QLabel#summaryInfo {
    font-size: 12px;
    color: #475569;
}

/* ================= RESULTADOS POR ITEM ================= */

QFrame#resultCard {
    background-color: #ffffff;
    border: none;
    border-bottom: 1px solid #e5e7eb;
    padding: 16px 0px;
    border-radius: 0px;
}

QLabel#resultTitle {
    font-size: 15px;
    font-weight: 700;
    color: #111827;
}

QLabel#resultSubtitle {
    font-size: 13px;
    color: #6b7280;
    margin-top: 4px;
}

/* ================= BADGES ================= */

QLabel#resultBadge {
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 13px;
    font-weight: 700;
    min-width: 70px;
    font-weight: 700;
}

QLabel#resultBadge[estado='ok'] {
    background-color: #dcfce7;
    color: #166534;
}

QLabel#resultBadge[estado='fail'] {
    background-color: #fee2e2;
    color: #991b1b;
}

/* ================= NOTAS ================= */

QLabel#noteText {
    color: #6b7280;
    font-size: 13px;
}

/* ================= SCROLL ================= */

QScrollArea {
    background-color: transparent;
    border: none;
}
QLabel#subSectionTitle {
    font-size: 18px;
    font-weight: 600;
    margin-top: 8px;
    background-color: transparent;
}
QLabel {
    background: transparent;
    border: none;
}


"""
