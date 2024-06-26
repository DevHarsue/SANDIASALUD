# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_usuarios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        if not Usuarios.objectName():
            Usuarios.setObjectName(u"Usuarios")
        Usuarios.resize(800, 600)
        Usuarios.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/logo.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        Usuarios.setWindowIcon(icon)
        Usuarios.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(Usuarios)
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
        self.boton_registrar = QPushButton(self.contenedor_principal)
        self.boton_registrar.setObjectName(u"boton_registrar")
        self.boton_registrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.boton_registrar, 7, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_usuario = QLineEdit(self.contenedor_principal)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_usuario, 4, 0, 1, 1)

        self.label_2 = QLabel(self.contenedor_principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 24px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.contenedor_principal)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(427, 240))
        self.label.setPixmap(QPixmap(u"images/logo_completo.jpeg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.combo_tipo = QComboBox(self.contenedor_principal)
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.setObjectName(u"combo_tipo")
        self.combo_tipo.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_tipo.setStyleSheet(u"min-width:8em;")

        self.gridLayout.addWidget(self.combo_tipo, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_confirmacion = QLineEdit(self.contenedor_principal)
        self.line_confirmacion.setObjectName(u"line_confirmacion")
        self.line_confirmacion.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_confirmacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_confirmacion, 6, 0, 1, 1)

        self.line_contrasena = QLineEdit(self.contenedor_principal)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_contrasena, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.boton_volver = QPushButton(self.contenedor_principal)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setEnabled(False)
        self.boton_volver.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.boton_volver, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        Usuarios.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.combo_tipo, self.line_usuario)
        QWidget.setTabOrder(self.line_usuario, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.line_confirmacion)
        QWidget.setTabOrder(self.line_confirmacion, self.boton_registrar)

        self.retranslateUi(Usuarios)

        QMetaObject.connectSlotsByName(Usuarios)
    # setupUi

    def retranslateUi(self, Usuarios):
        Usuarios.setWindowTitle(QCoreApplication.translate("Usuarios", u"SANDIA SALUD", None))
        self.boton_registrar.setText(QCoreApplication.translate("Usuarios", u"REGISTRAR", None))
        self.line_usuario.setPlaceholderText(QCoreApplication.translate("Usuarios", u"USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("Usuarios", u"CONFIGURAR USUARIOS", None))
        self.label.setText("")
        self.combo_tipo.setItemText(0, QCoreApplication.translate("Usuarios", u"SUPER-ADMIN", None))
        self.combo_tipo.setItemText(1, QCoreApplication.translate("Usuarios", u"ADMIN", None))
        self.combo_tipo.setItemText(2, QCoreApplication.translate("Usuarios", u"USUARIO", None))

        self.line_confirmacion.setPlaceholderText(QCoreApplication.translate("Usuarios", u"REPITE LA CONTRASE\u00d1A", None))
        self.line_contrasena.setPlaceholderText(QCoreApplication.translate("Usuarios", u"CONTRASE\u00d1A", None))
        self.boton_volver.setText(QCoreApplication.translate("Usuarios", u"VOLVER", None))
    # retranslateUi

