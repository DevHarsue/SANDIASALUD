# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_configuracion.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Configuracion(object):
    def setupUi(self, Configuracion):
        if not Configuracion.objectName():
            Configuracion.setObjectName(u"Configuracion")
        Configuracion.resize(800, 600)
        Configuracion.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/logo.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        Configuracion.setWindowIcon(icon)
        Configuracion.setStyleSheet(u"*{\n"
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
"	background: #ffffff;\n"
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
"\n"
"QMessageBox{\n"
"	background:white;\n"
"	color:#2C0146;\n"
"}\n"
"\n"
"QMessageBo"
                        "x QLabel{\n"
"	color:#2C0146;\n"
"}")
        self.centralwidget = QWidget(Configuracion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setStyleSheet(u"QLabel{\n"
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
"QLineEdit:disabled, QTextEdit:disabled,QPushButton:disabled,QDateEdit:disabled{\n"
"	background: rgb(235, 235, 235);\n"
"	border-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus{\n"
"	color: #60029a;\n"
"	border-color: #60029a;\n"
"}\n"
"\n"
"QDateEdit{\n"
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
"QScrollBar:vertical {\n"
"        border: 1px soli"
                        "d white;\n"
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
"/*\n"
"#2C0146;\n"
"#60029a;\n"
"")
        self.gridLayout_2 = QGridLayout(self.contenedor_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_host = QLineEdit(self.contenedor_principal)
        self.line_host.setObjectName(u"line_host")
        self.line_host.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_host, 5, 0, 1, 1)

        self.boton_iniciar = QPushButton(self.contenedor_principal)
        self.boton_iniciar.setObjectName(u"boton_iniciar")
        self.boton_iniciar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.boton_iniciar, 7, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_usuario = QLineEdit(self.contenedor_principal)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_usuario, 3, 0, 1, 1)

        self.label = QLabel(self.contenedor_principal)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(427, 240))
        self.label.setPixmap(QPixmap(u"images/logo_completo.jpeg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.line_contrasena = QLineEdit(self.contenedor_principal)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_contrasena, 4, 0, 1, 1)

        self.label_2 = QLabel(self.contenedor_principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 24px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.line_puerto = QLineEdit(self.contenedor_principal)
        self.line_puerto.setObjectName(u"line_puerto")
        self.line_puerto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_puerto, 6, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.boton_volver = QPushButton(self.contenedor_principal)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setEnabled(False)
        self.boton_volver.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.boton_volver, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        Configuracion.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Configuracion)
        self.statusbar.setObjectName(u"statusbar")
        Configuracion.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.line_usuario, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.line_host)
        QWidget.setTabOrder(self.line_host, self.line_puerto)
        QWidget.setTabOrder(self.line_puerto, self.boton_iniciar)

        self.retranslateUi(Configuracion)

        QMetaObject.connectSlotsByName(Configuracion)
    # setupUi

    def retranslateUi(self, Configuracion):
        Configuracion.setWindowTitle(QCoreApplication.translate("Configuracion", u"SANDIA SALUD", None))
        self.line_host.setPlaceholderText(QCoreApplication.translate("Configuracion", u"HOST", None))
        self.boton_iniciar.setText(QCoreApplication.translate("Configuracion", u"ACEPTAR", None))
        self.line_usuario.setPlaceholderText(QCoreApplication.translate("Configuracion", u"USUARIO", None))
        self.label.setText("")
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("Configuracion", u"CONTRASE\u00d1A", None))
        self.label_2.setText(QCoreApplication.translate("Configuracion", u"CONFIGURAR CONEXION CON LA BASE DE DATOS", None))
        self.line_puerto.setPlaceholderText(QCoreApplication.translate("Configuracion", u"PUERTO", None))
        self.boton_volver.setText(QCoreApplication.translate("Configuracion", u"VOLVER", None))
    # retranslateUi

