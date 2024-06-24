# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_SANDIASALUD(object):
    def setupUi(self, SANDIASALUD):
        if not SANDIASALUD.objectName():
            SANDIASALUD.setObjectName(u"SANDIASALUD")
        SANDIASALUD.setEnabled(True)
        SANDIASALUD.resize(800, 600)
        SANDIASALUD.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/logo.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        SANDIASALUD.setWindowIcon(icon)
        SANDIASALUD.setStyleSheet(u"*{\n"
"	font-family: Agency FB;\n"
"	font-weight: bold;\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background: qlineargradient(spread:pad, x1:0.438778, y1:1, x2:0.495, y2:0, stop:0 rgba(67, 37, 70, 255), stop:1 rgba(44, 1, 70, 255))\n"
"}\n"
"\n"
"#contenedor_principal{\n"
"	background: white;\n"
"	border-radius: 1em;\n"
"	\n"
"}\n"
"\n"
"#LOGO{\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: #2C0146;\n"
"	border:none;\n"
"	border-left: 2px solid #2C0146;\n"
"	border-right: 2px solid #2C0146;\n"
"	padding: 0.1em 0.8em;\n"
"}\n"
"\n"
"QPushButton:hover,QPushButton:focus{\n"
"	color: #60029a;\n"
"	border-color: #60029a;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: black;\n"
"	border-color: black;\n"
"}\n"
"\n"
"QStackedWidget{\n"
"	background: transparent;\n"
"	border: 2px solid #2C0146;\n"
"	border-radius: 0.5em;\n"
"}\n"
"\n"
"QStackedWidget QWidget{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QMessageBox{\n"
"	background:white;\n"
"	color:#2C0146;\n"
"}\n"
"\n"
"QMessageBox QLabe"
                        "l{\n"
"	color:#2C0146;\n"
"}")
        self.centralwidget = QWidget(SANDIASALUD)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.gridLayout = QGridLayout(self.contenedor_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_menu = QWidget(self.contenedor_principal)
        self.widget_menu.setObjectName(u"widget_menu")
        self.verticalLayout_2 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.boton_v_consulta = QPushButton(self.widget_menu)
        self.boton_v_consulta.setObjectName(u"boton_v_consulta")
        self.boton_v_consulta.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_consulta)

        self.boton_v_citas = QPushButton(self.widget_menu)
        self.boton_v_citas.setObjectName(u"boton_v_citas")
        self.boton_v_citas.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_citas)

        self.boton_v_agendar = QPushButton(self.widget_menu)
        self.boton_v_agendar.setObjectName(u"boton_v_agendar")
        self.boton_v_agendar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_agendar)

        self.boton_v_pacientes = QPushButton(self.widget_menu)
        self.boton_v_pacientes.setObjectName(u"boton_v_pacientes")
        self.boton_v_pacientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_pacientes)

        self.boton_v_registrar_pacientes = QPushButton(self.widget_menu)
        self.boton_v_registrar_pacientes.setObjectName(u"boton_v_registrar_pacientes")
        self.boton_v_registrar_pacientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_registrar_pacientes)

        self.boton_v_consultas = QPushButton(self.widget_menu)
        self.boton_v_consultas.setObjectName(u"boton_v_consultas")
        self.boton_v_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_consultas)


        self.gridLayout.addWidget(self.widget_menu, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.verticalLayout = QVBoxLayout(self.contenedor_logo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.boton_inicio = QPushButton(self.contenedor_logo)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_inicio.setStyleSheet(u"image: url(\"images/logo_sin_fondo.png\");\n"
"width:80px;\n"
"height:80px;\n"
"border:none;")

        self.verticalLayout.addWidget(self.boton_inicio)


        self.gridLayout.addWidget(self.contenedor_logo, 0, 0, 1, 1)

        self.widget_opciones = QWidget(self.contenedor_principal)
        self.widget_opciones.setObjectName(u"widget_opciones")
        self.horizontalLayout = QHBoxLayout(self.widget_opciones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_v_configuracion = QPushButton(self.widget_opciones)
        self.boton_v_configuracion.setObjectName(u"boton_v_configuracion")
        self.boton_v_configuracion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_configuracion)

        self.boton_v_cerrar_sesion = QPushButton(self.widget_opciones)
        self.boton_v_cerrar_sesion.setObjectName(u"boton_v_cerrar_sesion")
        self.boton_v_cerrar_sesion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_cerrar_sesion)


        self.gridLayout.addWidget(self.widget_opciones, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"QLabel{\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled{\n"
"	image: url(\"images/disabled.png\");\n"
"	width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"images/check.png\");\n"
"	width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(\"images/unchecked.png\");\n"
"	width: 16px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background: white;\n"
"	border: none;\n"
"	min-width: 2em;\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border: 1px dashed  #2C0146;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	background: white;\n"
"	border: none;\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	border: none;\n"
"	border-left: 2px solid #2C0146;\n"
"	outline: none;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit{\n"
"	background: white;\n"
"	color:	#2C0146;\n"
"	border: none;\n"
"	border-bottom: 2px solid "
                        "#2C0146;\n"
"}\n"
"\n"
"QLineEdit:disabled, QTextEdit:disabled,QPushButton:disabled,QDateEdit:disabled,QDateTimeEdit:disabled{\n"
"	background: rgb(205, 205, 205);\n"
"	border-color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus{\n"
"	color: #60029a;\n"
"	border-color: #60029a;\n"
"}\n"
"\n"
"QDateEdit,QDateTimeEdit{\n"
"	padding-right:1em;\n"
"	min-width: 6em;\n"
"	background: white;\n"
"	color: #2C0146;\n"
"	border: none;\n"
"	border-bottom: 2px solid #2C0146;\n"
"}\n"
"\n"
"QCalendarWidget{\n"
"	min-width:12em;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: #60029a;\n"
"	background-color: #2C0146;\n"
"	color: white;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"	qproperty-icon:url(\"images/left-arrow.png\");\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"	qproperty-icon:url(\"images/right-arrow.png\");\n"
"}\n"
"\n"
"#qt_calendar_navigationbar QSpinBox{\n"
"	min-width:4em;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background: transparent;\n"
"\n"
"}\n"
"\n"
"QScrollBar:ve"
                        "rtical {\n"
"        border: 1px solid white;\n"
"        width:10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
" background: #2C0146;\n"
"min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"Line{\n"
"	background: #2C0146;\n"
"}\n"
"\n"
"QTableView{\n"
"	padding: 0.5em;\n"
"	border: 2px solid #2C0146;\n"
"	border-radius: 5px;\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background:#2C0146;\n"
"	color:white;\n"
"}\n"
"\n"
"QTableView QHeaderView{\n"
"	color: #2C0146;\n"
"}\n"
"")
        self.widget_citas = QWidget()
        self.widget_citas.setObjectName(u"widget_citas")
        self.verticalLayout_5 = QVBoxLayout(self.widget_citas)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(24)
        self.gridLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.date_cita_desde = QDateEdit(self.widget_citas)
        self.date_cita_desde.setObjectName(u"date_cita_desde")
        self.date_cita_desde.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_cita_desde.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.date_cita_desde, 1, 1, 1, 1)

        self.label_21 = QLabel(self.widget_citas)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_22 = QLabel(self.widget_citas)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.date_cita_hasta = QDateEdit(self.widget_citas)
        self.date_cita_hasta.setObjectName(u"date_cita_hasta")
        self.date_cita_hasta.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_cita_hasta.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.date_cita_hasta, 3, 1, 1, 1)

        self.boton_buscar_cita = QPushButton(self.widget_citas)
        self.boton_buscar_cita.setObjectName(u"boton_buscar_cita")
        self.boton_buscar_cita.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_buscar_cita.setStyleSheet(u"icon: url(\"images/search.png\");")
        icon1 = QIcon(QIcon.fromTheme(u"system-search"))
        self.boton_buscar_cita.setIcon(icon1)

        self.gridLayout_7.addWidget(self.boton_buscar_cita, 1, 2, 2, 1, Qt.AlignmentFlag.AlignVCenter)

        self.check_rango_cita = QCheckBox(self.widget_citas)
        self.check_rango_cita.setObjectName(u"check_rango_cita")
        self.check_rango_cita.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.check_rango_cita, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 3)

        self.tabla_citas = QTableWidget(self.widget_citas)
        if (self.tabla_citas.columnCount() < 5):
            self.tabla_citas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_citas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_citas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_citas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_citas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tabla_citas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_citas.setObjectName(u"tabla_citas")
        self.tabla_citas.setEnabled(True)
        self.tabla_citas.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tabla_citas.setStyleSheet(u"")
        self.tabla_citas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tabla_citas.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tabla_citas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_citas.setAlternatingRowColors(True)
        self.tabla_citas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_citas.setShowGrid(False)
        self.tabla_citas.setGridStyle(Qt.PenStyle.SolidLine)
        self.tabla_citas.setCornerButtonEnabled(True)
        self.tabla_citas.setRowCount(0)
        self.tabla_citas.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_citas.horizontalHeader().setHighlightSections(True)
        self.tabla_citas.horizontalHeader().setStretchLastSection(True)
        self.tabla_citas.verticalHeader().setVisible(False)
        self.tabla_citas.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tabla_citas, 1, 0, 1, 3)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.stacked_widget.addWidget(self.widget_citas)
        self.widget_registrar_pacientes = QWidget()
        self.widget_registrar_pacientes.setObjectName(u"widget_registrar_pacientes")
        self.widget_registrar_pacientes.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_registrar_pacientes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_cedula = QLineEdit(self.widget_registrar_pacientes)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_cedula, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.boton_registrar = QPushButton(self.widget_registrar_pacientes)
        self.boton_registrar.setObjectName(u"boton_registrar")
        self.boton_registrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.boton_registrar, 6, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_apellido = QLineEdit(self.widget_registrar_pacientes)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_apellido, 1, 2, 1, 1)

        self.line_nombre = QLineEdit(self.widget_registrar_pacientes)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_nombre, 1, 1, 1, 1)

        self.text_direccion = QTextEdit(self.widget_registrar_pacientes)
        self.text_direccion.setObjectName(u"text_direccion")
        self.text_direccion.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.text_direccion, 5, 1, 1, 2)

        self.nacionalidad = QComboBox(self.widget_registrar_pacientes)
        self.nacionalidad.addItem("")
        self.nacionalidad.addItem("")
        self.nacionalidad.setObjectName(u"nacionalidad")
        self.nacionalidad.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.nacionalidad, 0, 0, 1, 1)

        self.line_telefono = QLineEdit(self.widget_registrar_pacientes)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_telefono, 4, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.fecha_nacimiento = QDateEdit(self.widget_registrar_pacientes)
        self.fecha_nacimiento.setObjectName(u"fecha_nacimiento")
        self.fecha_nacimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.fecha_nacimiento.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.fecha_nacimiento, 3, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_20 = QLabel(self.widget_registrar_pacientes)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 2, 1, 1, 2, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.widget_registrar_pacientes)
        self.widget_inicio = QWidget()
        self.widget_inicio.setObjectName(u"widget_inicio")
        self.verticalLayout_18 = QVBoxLayout(self.widget_inicio)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.widget_inicio)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"image:url(\"images/logo_completo.jpeg\")")
        self.label_16.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_16)

        self.stacked_widget.addWidget(self.widget_inicio)
        self.widget_consultas = QWidget()
        self.widget_consultas.setObjectName(u"widget_consultas")
        self.verticalLayout_20 = QVBoxLayout(self.widget_consultas)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.text_tratamiento_edit = QTextEdit(self.widget_consultas)
        self.text_tratamiento_edit.setObjectName(u"text_tratamiento_edit")
        self.text_tratamiento_edit.setEnabled(False)

        self.gridLayout_4.addWidget(self.text_tratamiento_edit, 4, 0, 1, 3)

        self.combo_nacionalidad_consultas = QComboBox(self.widget_consultas)
        self.combo_nacionalidad_consultas.addItem("")
        self.combo_nacionalidad_consultas.addItem("")
        self.combo_nacionalidad_consultas.setObjectName(u"combo_nacionalidad_consultas")
        self.combo_nacionalidad_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.combo_nacionalidad_consultas, 0, 0, 1, 1)

        self.text_diagnostico_edit = QTextEdit(self.widget_consultas)
        self.text_diagnostico_edit.setObjectName(u"text_diagnostico_edit")
        self.text_diagnostico_edit.setEnabled(False)

        self.gridLayout_4.addWidget(self.text_diagnostico_edit, 3, 0, 1, 3)

        self.boton_buscar_consultas = QPushButton(self.widget_consultas)
        self.boton_buscar_consultas.setObjectName(u"boton_buscar_consultas")
        self.boton_buscar_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_buscar_consultas, 0, 2, 1, 1)

        self.table_consultas = QTableWidget(self.widget_consultas)
        if (self.table_consultas.columnCount() < 4):
            self.table_consultas.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_consultas.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_consultas.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_consultas.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_consultas.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.table_consultas.setObjectName(u"table_consultas")
        self.table_consultas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_consultas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_consultas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_consultas.setAlternatingRowColors(True)
        self.table_consultas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_consultas.setShowGrid(False)
        self.table_consultas.setRowCount(0)
        self.table_consultas.horizontalHeader().setCascadingSectionResizes(False)
        self.table_consultas.horizontalHeader().setDefaultSectionSize(133)
        self.table_consultas.horizontalHeader().setHighlightSections(False)
        self.table_consultas.horizontalHeader().setStretchLastSection(True)
        self.table_consultas.verticalHeader().setVisible(False)
        self.table_consultas.verticalHeader().setHighlightSections(False)

        self.gridLayout_4.addWidget(self.table_consultas, 1, 0, 1, 3)

        self.line_cedula_consultas = QLineEdit(self.widget_consultas)
        self.line_cedula_consultas.setObjectName(u"line_cedula_consultas")
        self.line_cedula_consultas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.line_cedula_consultas, 0, 1, 1, 1)

        self.check_editar_consultas = QCheckBox(self.widget_consultas)
        self.check_editar_consultas.setObjectName(u"check_editar_consultas")
        self.check_editar_consultas.setEnabled(False)
        self.check_editar_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.check_editar_consultas, 2, 0, 1, 3)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 3)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setRowStretch(4, 1)

        self.verticalLayout_20.addLayout(self.gridLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.boton_actualizar_consultas = QPushButton(self.widget_consultas)
        self.boton_actualizar_consultas.setObjectName(u"boton_actualizar_consultas")
        self.boton_actualizar_consultas.setEnabled(False)
        self.boton_actualizar_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.boton_actualizar_consultas)

        self.boton_borrar_consultas = QPushButton(self.widget_consultas)
        self.boton_borrar_consultas.setObjectName(u"boton_borrar_consultas")
        self.boton_borrar_consultas.setEnabled(False)
        self.boton_borrar_consultas.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.boton_borrar_consultas)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.stacked_widget.addWidget(self.widget_consultas)
        self.widget_pacientes = QWidget()
        self.widget_pacientes.setObjectName(u"widget_pacientes")
        self.verticalLayout_11 = QVBoxLayout(self.widget_pacientes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.widget_pacientes)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 588, 1407))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.contenedor_buscador = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_buscador.setObjectName(u"contenedor_buscador")
        self._2 = QHBoxLayout(self.contenedor_buscador)
        self._2.setObjectName(u"_2")
        self.combo_nacionalidad = QComboBox(self.contenedor_buscador)
        self.combo_nacionalidad.addItem("")
        self.combo_nacionalidad.addItem("")
        self.combo_nacionalidad.setObjectName(u"combo_nacionalidad")
        self.combo_nacionalidad.setCursor(QCursor(Qt.PointingHandCursor))

        self._2.addWidget(self.combo_nacionalidad)

        self.line_cedula_buscar = QLineEdit(self.contenedor_buscador)
        self.line_cedula_buscar.setObjectName(u"line_cedula_buscar")
        self.line_cedula_buscar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2.addWidget(self.line_cedula_buscar)

        self.boton_buscar = QPushButton(self.contenedor_buscador)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setCursor(QCursor(Qt.PointingHandCursor))

        self._2.addWidget(self.boton_buscar)


        self.verticalLayout_6.addWidget(self.contenedor_buscador)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.contenedor_datos = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_datos.setObjectName(u"contenedor_datos")
        self.contenedor_datos_personales = QGridLayout(self.contenedor_datos)
        self.contenedor_datos_personales.setObjectName(u"contenedor_datos_personales")
        self.label_9 = QLabel(self.contenedor_datos)
        self.label_9.setObjectName(u"label_9")

        self.contenedor_datos_personales.addWidget(self.label_9, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_editar = QLineEdit(self.contenedor_datos)
        self.line_nombre_editar.setObjectName(u"line_nombre_editar")
        self.line_nombre_editar.setEnabled(False)
        self.line_nombre_editar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.contenedor_datos_personales.addWidget(self.line_nombre_editar, 1, 0, 1, 1)

        self.line_telefono_editar = QLineEdit(self.contenedor_datos)
        self.line_telefono_editar.setObjectName(u"line_telefono_editar")
        self.line_telefono_editar.setEnabled(False)
        self.line_telefono_editar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.contenedor_datos_personales.addWidget(self.line_telefono_editar, 4, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.text_direccion_editar = QTextEdit(self.contenedor_datos)
        self.text_direccion_editar.setObjectName(u"text_direccion_editar")
        self.text_direccion_editar.setEnabled(False)
        self.text_direccion_editar.setMinimumSize(QSize(0, 80))
        self.text_direccion_editar.setTabChangesFocus(True)

        self.contenedor_datos_personales.addWidget(self.text_direccion_editar, 5, 0, 1, 2)

        self.line_apellido_editar = QLineEdit(self.contenedor_datos)
        self.line_apellido_editar.setObjectName(u"line_apellido_editar")
        self.line_apellido_editar.setEnabled(False)
        self.line_apellido_editar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.contenedor_datos_personales.addWidget(self.line_apellido_editar, 1, 1, 1, 1)

        self.date_fecha_nacimiento = QDateEdit(self.contenedor_datos)
        self.date_fecha_nacimiento.setObjectName(u"date_fecha_nacimiento")
        self.date_fecha_nacimiento.setEnabled(False)
        self.date_fecha_nacimiento.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_fecha_nacimiento.setCalendarPopup(True)

        self.contenedor_datos_personales.addWidget(self.date_fecha_nacimiento, 3, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.check_datos_personales = QCheckBox(self.contenedor_datos)
        self.check_datos_personales.setObjectName(u"check_datos_personales")
        self.check_datos_personales.setEnabled(False)
        self.check_datos_personales.setCursor(QCursor(Qt.PointingHandCursor))

        self.contenedor_datos_personales.addWidget(self.check_datos_personales, 0, 0, 1, 2)


        self.verticalLayout_6.addWidget(self.contenedor_datos)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.contenedor_cita = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_cita.setObjectName(u"contenedor_cita")
        self.verticalLayout_7 = QVBoxLayout(self.contenedor_cita)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.check_proxima_cita = QCheckBox(self.contenedor_cita)
        self.check_proxima_cita.setObjectName(u"check_proxima_cita")
        self.check_proxima_cita.setEnabled(False)
        self.check_proxima_cita.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.check_proxima_cita)

        self.date_proxima_cita = QDateTimeEdit(self.contenedor_cita)
        self.date_proxima_cita.setObjectName(u"date_proxima_cita")
        self.date_proxima_cita.setEnabled(False)
        self.date_proxima_cita.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_proxima_cita.setCalendarPopup(True)

        self.verticalLayout_7.addWidget(self.date_proxima_cita, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.contenedor_cita)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.contenedor_consulta = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_consulta.setObjectName(u"contenedor_consulta")
        self.verticalLayout_8 = QVBoxLayout(self.contenedor_consulta)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.check_consulta = QCheckBox(self.contenedor_consulta)
        self.check_consulta.setObjectName(u"check_consulta")
        self.check_consulta.setEnabled(False)
        self.check_consulta.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.check_consulta)

        self.label_6 = QLabel(self.contenedor_consulta)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.text_diagnostico = QTextEdit(self.contenedor_consulta)
        self.text_diagnostico.setObjectName(u"text_diagnostico")
        self.text_diagnostico.setEnabled(False)
        self.text_diagnostico.setMinimumSize(QSize(0, 80))
        self.text_diagnostico.setTabChangesFocus(True)

        self.verticalLayout_8.addWidget(self.text_diagnostico)

        self.label_8 = QLabel(self.contenedor_consulta)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.text_tratamiento_consulta = QTextEdit(self.contenedor_consulta)
        self.text_tratamiento_consulta.setObjectName(u"text_tratamiento_consulta")
        self.text_tratamiento_consulta.setEnabled(False)
        self.text_tratamiento_consulta.setMinimumSize(QSize(0, 80))
        self.text_tratamiento_consulta.setTabChangesFocus(True)

        self.verticalLayout_8.addWidget(self.text_tratamiento_consulta)


        self.verticalLayout_6.addWidget(self.contenedor_consulta)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_4)

        self.contenedor_antecedentes = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_antecedentes.setObjectName(u"contenedor_antecedentes")
        self.verticalLayout_9 = QVBoxLayout(self.contenedor_antecedentes)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.check_antecedentes = QCheckBox(self.contenedor_antecedentes)
        self.check_antecedentes.setObjectName(u"check_antecedentes")
        self.check_antecedentes.setEnabled(False)
        self.check_antecedentes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.check_antecedentes)

        self.label_3 = QLabel(self.contenedor_antecedentes)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.text_patologicos = QTextEdit(self.contenedor_antecedentes)
        self.text_patologicos.setObjectName(u"text_patologicos")
        self.text_patologicos.setEnabled(False)
        self.text_patologicos.setMinimumSize(QSize(0, 80))
        self.text_patologicos.setTabChangesFocus(True)

        self.verticalLayout_9.addWidget(self.text_patologicos)

        self.label_4 = QLabel(self.contenedor_antecedentes)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.text_quirurjicos = QTextEdit(self.contenedor_antecedentes)
        self.text_quirurjicos.setObjectName(u"text_quirurjicos")
        self.text_quirurjicos.setEnabled(False)
        self.text_quirurjicos.setMinimumSize(QSize(0, 80))
        self.text_quirurjicos.setTabChangesFocus(True)

        self.verticalLayout_9.addWidget(self.text_quirurjicos)

        self.label_5 = QLabel(self.contenedor_antecedentes)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.text_tratamiento = QTextEdit(self.contenedor_antecedentes)
        self.text_tratamiento.setObjectName(u"text_tratamiento")
        self.text_tratamiento.setEnabled(False)
        self.text_tratamiento.setMinimumSize(QSize(0, 80))
        self.text_tratamiento.setTabChangesFocus(True)

        self.verticalLayout_9.addWidget(self.text_tratamiento)

        self.label_7 = QLabel(self.contenedor_antecedentes)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_relaciones = QDateEdit(self.contenedor_antecedentes)
        self.date_relaciones.setObjectName(u"date_relaciones")
        self.date_relaciones.setEnabled(False)
        self.date_relaciones.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_relaciones.setCalendarPopup(True)

        self.verticalLayout_9.addWidget(self.date_relaciones, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.contenedor_antecedentes)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.contenedor_datos_embarazo = QWidget(self.scrollAreaWidgetContents)
        self.contenedor_datos_embarazo.setObjectName(u"contenedor_datos_embarazo")
        self.contenedor_datos_embarazo.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_10 = QVBoxLayout(self.contenedor_datos_embarazo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.check_embarazo = QCheckBox(self.contenedor_datos_embarazo)
        self.check_embarazo.setObjectName(u"check_embarazo")
        self.check_embarazo.setEnabled(False)
        self.check_embarazo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.check_embarazo)

        self.label = QLabel(self.contenedor_datos_embarazo)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_ultima_regla = QDateEdit(self.contenedor_datos_embarazo)
        self.date_ultima_regla.setObjectName(u"date_ultima_regla")
        self.date_ultima_regla.setEnabled(False)
        self.date_ultima_regla.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_ultima_regla.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.date_ultima_regla, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.contenedor_datos_embarazo)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_parto = QDateEdit(self.contenedor_datos_embarazo)
        self.date_parto.setObjectName(u"date_parto")
        self.date_parto.setEnabled(False)
        self.date_parto.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_parto.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.date_parto, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.contenedor_datos_embarazo)

        self.boton_borrar_paciente = QPushButton(self.scrollAreaWidgetContents)
        self.boton_borrar_paciente.setObjectName(u"boton_borrar_paciente")
        self.boton_borrar_paciente.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.boton_borrar_paciente, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_actualizar_datos = QPushButton(self.widget_pacientes)
        self.boton_actualizar_datos.setObjectName(u"boton_actualizar_datos")
        self.boton_actualizar_datos.setEnabled(False)
        self.boton_actualizar_datos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.boton_actualizar_datos)

        self.boton_imprimir = QPushButton(self.widget_pacientes)
        self.boton_imprimir.setObjectName(u"boton_imprimir")
        self.boton_imprimir.setEnabled(False)
        self.boton_imprimir.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.boton_imprimir)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.stacked_widget.addWidget(self.widget_pacientes)
        self.widget_registrar_antecedente = QWidget()
        self.widget_registrar_antecedente.setObjectName(u"widget_registrar_antecedente")
        self.verticalLayout_16 = QVBoxLayout(self.widget_registrar_antecedente)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.widget_registrar_antecedente)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.widget_registrar_antecedente)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_15.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_primera_relacion = QDateEdit(self.widget_registrar_antecedente)
        self.date_primera_relacion.setObjectName(u"date_primera_relacion")
        self.date_primera_relacion.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_primera_relacion.setCalendarPopup(True)

        self.verticalLayout_15.addWidget(self.date_primera_relacion, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.text_antecedente_patologico_registro = QTextEdit(self.widget_registrar_antecedente)
        self.text_antecedente_patologico_registro.setObjectName(u"text_antecedente_patologico_registro")
        self.text_antecedente_patologico_registro.setTabChangesFocus(True)

        self.verticalLayout_15.addWidget(self.text_antecedente_patologico_registro)

        self.text_antecedente_quirurjico_registro = QTextEdit(self.widget_registrar_antecedente)
        self.text_antecedente_quirurjico_registro.setObjectName(u"text_antecedente_quirurjico_registro")
        self.text_antecedente_quirurjico_registro.setTabChangesFocus(True)

        self.verticalLayout_15.addWidget(self.text_antecedente_quirurjico_registro)

        self.text_tratamiento_registro = QTextEdit(self.widget_registrar_antecedente)
        self.text_tratamiento_registro.setObjectName(u"text_tratamiento_registro")
        self.text_tratamiento_registro.setTabChangesFocus(True)

        self.verticalLayout_15.addWidget(self.text_tratamiento_registro)

        self.boton_registrar_antecedentes = QPushButton(self.widget_registrar_antecedente)
        self.boton_registrar_antecedentes.setObjectName(u"boton_registrar_antecedentes")
        self.boton_registrar_antecedentes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_15.addWidget(self.boton_registrar_antecedentes, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.stacked_widget.addWidget(self.widget_registrar_antecedente)
        self.widget_agendar_cita = QWidget()
        self.widget_agendar_cita.setObjectName(u"widget_agendar_cita")
        self.verticalLayout_17 = QVBoxLayout(self.widget_agendar_cita)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.combo_nacionalidad_agenda = QComboBox(self.widget_agendar_cita)
        self.combo_nacionalidad_agenda.addItem("")
        self.combo_nacionalidad_agenda.addItem("")
        self.combo_nacionalidad_agenda.setObjectName(u"combo_nacionalidad_agenda")
        self.combo_nacionalidad_agenda.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.combo_nacionalidad_agenda, 0, 0, 1, 1)

        self.line_cedula_agenda = QLineEdit(self.widget_agendar_cita)
        self.line_cedula_agenda.setObjectName(u"line_cedula_agenda")
        self.line_cedula_agenda.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.line_cedula_agenda, 0, 1, 1, 1)

        self.boton_buscar_agenda = QPushButton(self.widget_agendar_cita)
        self.boton_buscar_agenda.setObjectName(u"boton_buscar_agenda")
        self.boton_buscar_agenda.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.boton_buscar_agenda, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_nombre_agenda = QLineEdit(self.widget_agendar_cita)
        self.line_nombre_agenda.setObjectName(u"line_nombre_agenda")
        self.line_nombre_agenda.setEnabled(False)
        self.line_nombre_agenda.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.line_nombre_agenda)

        self.line_apellido_agenda = QLineEdit(self.widget_agendar_cita)
        self.line_apellido_agenda.setObjectName(u"line_apellido_agenda")
        self.line_apellido_agenda.setEnabled(False)
        self.line_apellido_agenda.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.line_apellido_agenda)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)

        self.label_15 = QLabel(self.widget_agendar_cita)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 3)

        self.boton_agendar = QPushButton(self.widget_agendar_cita)
        self.boton_agendar.setObjectName(u"boton_agendar")
        self.boton_agendar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.boton_agendar, 4, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.date_agenda = QDateTimeEdit(self.widget_agendar_cita)
        self.date_agenda.setObjectName(u"date_agenda")
        self.date_agenda.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_agenda.setCalendarPopup(True)

        self.gridLayout_6.addWidget(self.date_agenda, 3, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_17.addLayout(self.gridLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)

        self.stacked_widget.addWidget(self.widget_agendar_cita)
        self.widget_consulta = QWidget()
        self.widget_consulta.setObjectName(u"widget_consulta")
        self.verticalLayout_12 = QVBoxLayout(self.widget_consulta)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_2 = QScrollArea(self.widget_consulta)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -171, 588, 587))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.consulta_antecedentes = QWidget(self.scrollAreaWidgetContents_2)
        self.consulta_antecedentes.setObjectName(u"consulta_antecedentes")
        self.consulta_antecedentes.setMaximumSize(QSize(16777215, 0))
        self.consulta_antecedentes.setBaseSize(QSize(0, 0))
        self.verticalLayout_14 = QVBoxLayout(self.consulta_antecedentes)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.consulta_antecedentes)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_14.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_primera_relacion_consulta = QDateEdit(self.consulta_antecedentes)
        self.date_primera_relacion_consulta.setObjectName(u"date_primera_relacion_consulta")
        self.date_primera_relacion_consulta.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_primera_relacion_consulta.setCalendarPopup(True)

        self.verticalLayout_14.addWidget(self.date_primera_relacion_consulta, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.consulta_antecedentes)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)

        self.text_antecedente_patologico = QTextEdit(self.consulta_antecedentes)
        self.text_antecedente_patologico.setObjectName(u"text_antecedente_patologico")
        self.text_antecedente_patologico.setMinimumSize(QSize(0, 80))
        self.text_antecedente_patologico.setTabChangesFocus(True)

        self.verticalLayout_14.addWidget(self.text_antecedente_patologico)

        self.label_12 = QLabel(self.consulta_antecedentes)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.text_antecedentes_quirurjicos = QTextEdit(self.consulta_antecedentes)
        self.text_antecedentes_quirurjicos.setObjectName(u"text_antecedentes_quirurjicos")
        self.text_antecedentes_quirurjicos.setMinimumSize(QSize(0, 80))
        self.text_antecedentes_quirurjicos.setTabChangesFocus(True)

        self.verticalLayout_14.addWidget(self.text_antecedentes_quirurjicos)

        self.label_13 = QLabel(self.consulta_antecedentes)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.text_tratamiento_actual = QTextEdit(self.consulta_antecedentes)
        self.text_tratamiento_actual.setObjectName(u"text_tratamiento_actual")
        self.text_tratamiento_actual.setMinimumSize(QSize(0, 80))
        self.text_tratamiento_actual.setTabChangesFocus(True)

        self.verticalLayout_14.addWidget(self.text_tratamiento_actual)


        self.gridLayout_5.addWidget(self.consulta_antecedentes, 5, 0, 1, 4)

        self.text_consulta_tratamiento = QTextEdit(self.scrollAreaWidgetContents_2)
        self.text_consulta_tratamiento.setObjectName(u"text_consulta_tratamiento")
        self.text_consulta_tratamiento.setMinimumSize(QSize(0, 80))
        self.text_consulta_tratamiento.setTabChangesFocus(True)

        self.gridLayout_5.addWidget(self.text_consulta_tratamiento, 10, 0, 1, 4)

        self.combo_consulta_antecedentes = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_consulta_antecedentes.addItem("")
        self.combo_consulta_antecedentes.addItem("")
        self.combo_consulta_antecedentes.setObjectName(u"combo_consulta_antecedentes")
        self.combo_consulta_antecedentes.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_consulta_antecedentes.setStyleSheet(u"max-width:3em;")

        self.gridLayout_5.addWidget(self.combo_consulta_antecedentes, 0, 0, 1, 1)

        self.boton_ver_antecedentes = QPushButton(self.scrollAreaWidgetContents_2)
        self.boton_ver_antecedentes.setObjectName(u"boton_ver_antecedentes")
        self.boton_ver_antecedentes.setEnabled(True)
        self.boton_ver_antecedentes.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.boton_ver_antecedentes, 4, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.boton_consulta_cedula = QPushButton(self.scrollAreaWidgetContents_2)
        self.boton_consulta_cedula.setObjectName(u"boton_consulta_cedula")
        self.boton_consulta_cedula.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.boton_consulta_cedula, 0, 3, 1, 1)

        self.line_consulta_cedula = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_consulta_cedula.setObjectName(u"line_consulta_cedula")
        self.line_consulta_cedula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.line_consulta_cedula, 0, 1, 1, 2)

        self.line_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_8, 3, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_consulta_nombre = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_consulta_nombre.setObjectName(u"line_consulta_nombre")
        self.line_consulta_nombre.setEnabled(False)
        self.line_consulta_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.line_consulta_nombre)

        self.line_consulta_apellido = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_consulta_apellido.setObjectName(u"line_consulta_apellido")
        self.line_consulta_apellido.setEnabled(False)
        self.line_consulta_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.line_consulta_apellido)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 2, 0, 1, 4)

        self.text_consulta_diagnostico = QTextEdit(self.scrollAreaWidgetContents_2)
        self.text_consulta_diagnostico.setObjectName(u"text_consulta_diagnostico")
        self.text_consulta_diagnostico.setMinimumSize(QSize(0, 80))
        self.text_consulta_diagnostico.setTabChangesFocus(True)

        self.gridLayout_5.addWidget(self.text_consulta_diagnostico, 9, 0, 1, 4)

        self.line_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_9, 6, 0, 1, 4)


        self.verticalLayout_13.addLayout(self.gridLayout_5)

        self.check_proxima_cita_consulta = QCheckBox(self.scrollAreaWidgetContents_2)
        self.check_proxima_cita_consulta.setObjectName(u"check_proxima_cita_consulta")
        self.check_proxima_cita_consulta.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.check_proxima_cita_consulta)

        self.date_proxima_cita_consulta = QDateTimeEdit(self.scrollAreaWidgetContents_2)
        self.date_proxima_cita_consulta.setObjectName(u"date_proxima_cita_consulta")
        self.date_proxima_cita_consulta.setEnabled(False)
        self.date_proxima_cita_consulta.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_proxima_cita_consulta.setCalendarPopup(True)

        self.verticalLayout_13.addWidget(self.date_proxima_cita_consulta, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_7)

        self.check_embarazo_consulta = QCheckBox(self.scrollAreaWidgetContents_2)
        self.check_embarazo_consulta.setObjectName(u"check_embarazo_consulta")
        self.check_embarazo_consulta.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.check_embarazo_consulta)

        self.contenedor_embarazo = QWidget(self.scrollAreaWidgetContents_2)
        self.contenedor_embarazo.setObjectName(u"contenedor_embarazo")
        self.verticalLayout_19 = QVBoxLayout(self.contenedor_embarazo)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.contenedor_embarazo)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_19.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_consulta_ultima_regla = QDateEdit(self.contenedor_embarazo)
        self.date_consulta_ultima_regla.setObjectName(u"date_consulta_ultima_regla")
        self.date_consulta_ultima_regla.setEnabled(False)
        self.date_consulta_ultima_regla.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_consulta_ultima_regla.setCalendarPopup(True)

        self.verticalLayout_19.addWidget(self.date_consulta_ultima_regla, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_19 = QLabel(self.contenedor_embarazo)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_19.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.date_consulta_parto = QDateEdit(self.contenedor_embarazo)
        self.date_consulta_parto.setObjectName(u"date_consulta_parto")
        self.date_consulta_parto.setEnabled(False)
        self.date_consulta_parto.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_consulta_parto.setCalendarPopup(True)

        self.verticalLayout_19.addWidget(self.date_consulta_parto, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_13.addWidget(self.contenedor_embarazo)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.scrollArea_2)

        self.boton_fin_consulta = QPushButton(self.widget_consulta)
        self.boton_fin_consulta.setObjectName(u"boton_fin_consulta")
        self.boton_fin_consulta.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.boton_fin_consulta, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stacked_widget.addWidget(self.widget_consulta)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        SANDIASALUD.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.boton_v_citas, self.boton_v_pacientes)
        QWidget.setTabOrder(self.boton_v_pacientes, self.boton_v_registrar_pacientes)
        QWidget.setTabOrder(self.boton_v_registrar_pacientes, self.nacionalidad)
        QWidget.setTabOrder(self.nacionalidad, self.line_cedula)
        QWidget.setTabOrder(self.line_cedula, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apellido)
        QWidget.setTabOrder(self.line_apellido, self.fecha_nacimiento)
        QWidget.setTabOrder(self.fecha_nacimiento, self.line_telefono)
        QWidget.setTabOrder(self.line_telefono, self.text_direccion)
        QWidget.setTabOrder(self.text_direccion, self.boton_registrar)
        QWidget.setTabOrder(self.boton_registrar, self.boton_v_configuracion)
        QWidget.setTabOrder(self.boton_v_configuracion, self.boton_v_cerrar_sesion)

        self.retranslateUi(SANDIASALUD)

        self.stacked_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(SANDIASALUD)
    # setupUi

    def retranslateUi(self, SANDIASALUD):
        SANDIASALUD.setWindowTitle(QCoreApplication.translate("SANDIASALUD", u"SANDIA SALUD", None))
        self.boton_v_consulta.setText(QCoreApplication.translate("SANDIASALUD", u"CONSULTA", None))
        self.boton_v_citas.setText(QCoreApplication.translate("SANDIASALUD", u"CITAS", None))
        self.boton_v_agendar.setText(QCoreApplication.translate("SANDIASALUD", u"AGENDAR\n"
"CITAS", None))
        self.boton_v_pacientes.setText(QCoreApplication.translate("SANDIASALUD", u"PACIENTES", None))
        self.boton_v_registrar_pacientes.setText(QCoreApplication.translate("SANDIASALUD", u"REGISTRAR\n"
"PACIENTES", None))
        self.boton_v_consultas.setText(QCoreApplication.translate("SANDIASALUD", u"VER\n"
"CONSULTAS", None))
        self.boton_inicio.setText("")
        self.boton_v_configuracion.setText(QCoreApplication.translate("SANDIASALUD", u"CONFIGURACI\u00d3N", None))
        self.boton_v_cerrar_sesion.setText(QCoreApplication.translate("SANDIASALUD", u"CERRAR SESI\u00d3N", None))
        self.label_21.setText(QCoreApplication.translate("SANDIASALUD", u"DESDE:", None))
        self.label_22.setText(QCoreApplication.translate("SANDIASALUD", u"HASTA:", None))
        self.boton_buscar_cita.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR", None))
        self.check_rango_cita.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR POR RANGO", None))
        ___qtablewidgetitem = self.tabla_citas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SANDIASALUD", u"NACIONALIDAD", None));
        ___qtablewidgetitem1 = self.tabla_citas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None));
        ___qtablewidgetitem2 = self.tabla_citas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SANDIASALUD", u"NOMBRE", None));
        ___qtablewidgetitem3 = self.tabla_citas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SANDIASALUD", u"APELLIDO", None));
        ___qtablewidgetitem4 = self.tabla_citas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SANDIASALUD", u"CITA", None));
        self.line_cedula.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None))
        self.boton_registrar.setText(QCoreApplication.translate("SANDIASALUD", u"REGISTRAR", None))
        self.line_apellido.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"APELLIDOS", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"NOMBRES", None))
        self.text_direccion.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"DIRECCI\u00d3N", None))
        self.nacionalidad.setItemText(0, QCoreApplication.translate("SANDIASALUD", u"V", None))
        self.nacionalidad.setItemText(1, QCoreApplication.translate("SANDIASALUD", u"E", None))

        self.line_telefono.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TELEFONO", None))
        self.label_20.setText(QCoreApplication.translate("SANDIASALUD", u"FECHA DE NACIMIENTO:", None))
        self.label_16.setText("")
        self.text_tratamiento_edit.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO", None))
        self.combo_nacionalidad_consultas.setItemText(0, QCoreApplication.translate("SANDIASALUD", u"V", None))
        self.combo_nacionalidad_consultas.setItemText(1, QCoreApplication.translate("SANDIASALUD", u"E", None))

        self.text_diagnostico_edit.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"DIAGNOSTICO", None))
        self.boton_buscar_consultas.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR", None))
        ___qtablewidgetitem5 = self.table_consultas.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SANDIASALUD", u"ID", None));
        ___qtablewidgetitem6 = self.table_consultas.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SANDIASALUD", u"NOMBRE", None));
        ___qtablewidgetitem7 = self.table_consultas.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SANDIASALUD", u"APELLIDO", None));
        ___qtablewidgetitem8 = self.table_consultas.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SANDIASALUD", u"FECHA", None));
        self.line_cedula_consultas.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None))
        self.check_editar_consultas.setText(QCoreApplication.translate("SANDIASALUD", u"ACTUALIZAR", None))
        self.boton_actualizar_consultas.setText(QCoreApplication.translate("SANDIASALUD", u"ACTUALIZAR", None))
        self.boton_borrar_consultas.setText(QCoreApplication.translate("SANDIASALUD", u"BORRAR", None))
        self.combo_nacionalidad.setItemText(0, QCoreApplication.translate("SANDIASALUD", u"V", None))
        self.combo_nacionalidad.setItemText(1, QCoreApplication.translate("SANDIASALUD", u"E", None))

        self.line_cedula_buscar.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None))
        self.boton_buscar.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR", None))
        self.label_9.setText(QCoreApplication.translate("SANDIASALUD", u"FECHA DE NACIMIENTO:", None))
        self.line_nombre_editar.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"NOMBRE", None))
        self.line_telefono_editar.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TELEFONO", None))
        self.text_direccion_editar.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"DIRECCION", None))
        self.line_apellido_editar.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"APELLIDO", None))
        self.check_datos_personales.setText(QCoreApplication.translate("SANDIASALUD", u"EDITAR DATOS PERSONALES", None))
        self.check_proxima_cita.setText(QCoreApplication.translate("SANDIASALUD", u"EDITAR PROXIMA CITA", None))
        self.check_consulta.setText(QCoreApplication.translate("SANDIASALUD", u"EDITAR ULTIMA CONSULTA", None))
        self.label_6.setText(QCoreApplication.translate("SANDIASALUD", u"DIAGNOSTICO:", None))
        self.text_diagnostico.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"DIAGNOSTICO", None))
        self.label_8.setText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO:", None))
        self.text_tratamiento_consulta.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO", None))
        self.check_antecedentes.setText(QCoreApplication.translate("SANDIASALUD", u"EDITAR ANTECEDENTES", None))
        self.label_3.setText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES PATOLOGICOS:", None))
        self.text_patologicos.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES PATOLOGICOS", None))
        self.label_4.setText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES QUIRURJICOS:", None))
        self.text_quirurjicos.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES QUIRURJICOS", None))
        self.label_5.setText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO:", None))
        self.text_tratamiento.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO", None))
        self.label_7.setText(QCoreApplication.translate("SANDIASALUD", u"PRIMERA RELACION SEXUAL:", None))
        self.check_embarazo.setText(QCoreApplication.translate("SANDIASALUD", u"EDITAR DATOS DE EMBARAZO", None))
        self.label.setText(QCoreApplication.translate("SANDIASALUD", u"ULTIMA REGLA:", None))
        self.label_2.setText(QCoreApplication.translate("SANDIASALUD", u"PARTO:", None))
        self.boton_borrar_paciente.setText(QCoreApplication.translate("SANDIASALUD", u"BORRAR PACIENTE", None))
        self.boton_actualizar_datos.setText(QCoreApplication.translate("SANDIASALUD", u"ACTUALIZAR", None))
        self.boton_imprimir.setText(QCoreApplication.translate("SANDIASALUD", u"IMPRIMIR", None))
        self.label_14.setText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES", None))
        self.label_17.setText(QCoreApplication.translate("SANDIASALUD", u"PRIMERA RELACI\u00d3N SEXUAL :", None))
        self.text_antecedente_patologico_registro.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES PATOLOGICOS", None))
        self.text_antecedente_quirurjico_registro.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES QUIRURJICOS", None))
        self.text_tratamiento_registro.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO ACTUAL", None))
        self.boton_registrar_antecedentes.setText(QCoreApplication.translate("SANDIASALUD", u"ACEPTAR", None))
        self.combo_nacionalidad_agenda.setItemText(0, QCoreApplication.translate("SANDIASALUD", u"V", None))
        self.combo_nacionalidad_agenda.setItemText(1, QCoreApplication.translate("SANDIASALUD", u"E", None))

        self.line_cedula_agenda.setText("")
        self.line_cedula_agenda.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None))
        self.boton_buscar_agenda.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR", None))
        self.line_nombre_agenda.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"NOMBRE", None))
        self.line_apellido_agenda.setText("")
        self.line_apellido_agenda.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"APELLIDO", None))
        self.label_15.setText(QCoreApplication.translate("SANDIASALUD", u"AGENDAR CITA PARA:", None))
        self.boton_agendar.setText(QCoreApplication.translate("SANDIASALUD", u"AGENDAR", None))
        self.label_10.setText(QCoreApplication.translate("SANDIASALUD", u"PRIMERA RELACI\u00d3N SEXUAL:", None))
        self.label_11.setText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES PATOLOGICOS:", None))
        self.text_antecedente_patologico.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES PATOLOGICOS", None))
        self.label_12.setText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES QUIRURJICOS:", None))
        self.text_antecedentes_quirurjicos.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"ANTECEDENTES QUIRURJICOS", None))
        self.label_13.setText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO:", None))
        self.text_tratamiento_actual.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO ACTUAL", None))
        self.text_consulta_tratamiento.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"TRATAMIENTO", None))
        self.combo_consulta_antecedentes.setItemText(0, QCoreApplication.translate("SANDIASALUD", u"V", None))
        self.combo_consulta_antecedentes.setItemText(1, QCoreApplication.translate("SANDIASALUD", u"E", None))

        self.boton_ver_antecedentes.setText(QCoreApplication.translate("SANDIASALUD", u"VER/EDITAR\n"
"ANTECEDENTES", None))
        self.boton_consulta_cedula.setText(QCoreApplication.translate("SANDIASALUD", u"BUSCAR", None))
        self.line_consulta_cedula.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"CEDULA", None))
        self.line_consulta_nombre.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"NOMBRE", None))
        self.line_consulta_apellido.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"APELLIDO", None))
        self.text_consulta_diagnostico.setPlaceholderText(QCoreApplication.translate("SANDIASALUD", u"DIAGNOSTICO", None))
        self.check_proxima_cita_consulta.setText(QCoreApplication.translate("SANDIASALUD", u"AGENDAR PROXIMA CITA", None))
        self.check_embarazo_consulta.setText(QCoreApplication.translate("SANDIASALUD", u"EMBARAZO", None))
        self.label_18.setText(QCoreApplication.translate("SANDIASALUD", u"ULTIMA REGLA:", None))
        self.label_19.setText(QCoreApplication.translate("SANDIASALUD", u"PARTO:", None))
        self.boton_fin_consulta.setText(QCoreApplication.translate("SANDIASALUD", u"FIN DE LA CONSULTA", None))
    # retranslateUi

