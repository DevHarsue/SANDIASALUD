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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"*{\n"
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
"#widget_menu QPushButton, #widget_opciones QPushButton,#boton_registrar{\n"
"	color: #2C0146;\n"
"	border:none;\n"
"	border-left: 2px solid #2C0146;\n"
"	border-right: 2px solid #2C0146;\n"
"	padding: 0.1em 0.8em;\n"
"}\n"
"\n"
"#widget_menu QPushButton:hover, #widget_opciones QPushButton:hover,#boton_registrar:hover,#widget_menu QPushButton:focus, #widget_opciones QPushButton:focus,#boton_registrar:focus{\n"
"	color: #60029a;\n"
"	border-color: #60029a;\n"
"}\n"
"\n"
"#widget_menu QPushButton:pressed, #widget_opciones QPushButton:pressed,#boton_registrar:pressed{\n"
"	color: black;\n"
"	border-color: black;\n"
"}\n"
""
                        "\n"
"#widget_registrar_pacientes,#widget_citas,#widget_pacientes{\n"
"	background: transparent;\n"
"	border: 2px solid #2C0146;\n"
"	border-radius: 0.5em;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
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
        self.pushButton = QPushButton(self.widget_menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.widget_menu, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.widget_opciones = QWidget(self.contenedor_principal)
        self.widget_opciones.setObjectName(u"widget_opciones")
        self.horizontalLayout = QHBoxLayout(self.widget_opciones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.widget_opciones)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_opciones)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.widget_opciones, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.verticalLayout = QVBoxLayout(self.contenedor_logo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LOGO = QLabel(self.contenedor_logo)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setMaximumSize(QSize(80, 80))
        self.LOGO.setPixmap(QPixmap(u"images/logo_sin_fondo.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.LOGO, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.contenedor_logo, 0, 0, 1, 1)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"#nacionalidad{\n"
"	background: white;\n"
"	border: none;\n"
"	min-width: 2em;\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"#nacionalidad:focus{\n"
"	border: 1px dashed  #2C0146;\n"
"}\n"
"\n"
"#nacionalidad QAbstractItemView{\n"
"	background: white;\n"
"	border: none;\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"#nacionalidad QAbstractItemView::item{\n"
"	color: #2C0146;\n"
"}\n"
"\n"
"#nacionalidad QAbstractItemView::item:selected {\n"
"	border: none;\n"
"	border-left: 2px solid #2C0146;\n"
"	outline: none;\n"
"}\n"
"\n"
"#widget_registrar_pacientes QLineEdit, #text_direccion{\n"
"	background: white;\n"
"	color:	#2C0146;\n"
"	border: none;\n"
"	border-bottom: 2px solid #2C0146;\n"
"}\n"
"\n"
"#widget_registrar_pacientes QLineEdit:focus, #text_direccion:focus{\n"
"	color: #60029a;\n"
"	border-color: #60029a;\n"
"}\n"
"\n"
"#fecha_nacimiento{\n"
"	min-width: 6em;\n"
"	background: transparent;\n"
"	color: #2C0146;\n"
"	border: none;\n"
"	border-bottom: 2px solid #2C0146;\n"
"}\n"
"\n"
"#boton_registrar{\n"
"	background: transpar"
                        "ent;\n"
"\n"
"}\n"
"\n"
"/*\n"
"#2C0146;\n"
"#60029a;\n"
"")
        self.widget_citas = QWidget()
        self.widget_citas.setObjectName(u"widget_citas")
        self.stacked_widget.addWidget(self.widget_citas)
        self.widget_registrar_pacientes = QWidget()
        self.widget_registrar_pacientes.setObjectName(u"widget_registrar_pacientes")
        self.widget_registrar_pacientes.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_registrar_pacientes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_apellido = QLineEdit(self.widget_registrar_pacientes)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_apellido, 1, 2, 1, 1)

        self.line_nombre = QLineEdit(self.widget_registrar_pacientes)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_nombre, 1, 1, 1, 1)

        self.boton_registrar = QPushButton(self.widget_registrar_pacientes)
        self.boton_registrar.setObjectName(u"boton_registrar")

        self.gridLayout_2.addWidget(self.boton_registrar, 5, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_telefono = QLineEdit(self.widget_registrar_pacientes)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_telefono, 3, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.text_direccion = QTextEdit(self.widget_registrar_pacientes)
        self.text_direccion.setObjectName(u"text_direccion")
        self.text_direccion.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.text_direccion, 4, 1, 1, 2)

        self.line_cedula = QLineEdit(self.widget_registrar_pacientes)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_cedula, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.fecha_nacimiento = QDateEdit(self.widget_registrar_pacientes)
        self.fecha_nacimiento.setObjectName(u"fecha_nacimiento")
        self.fecha_nacimiento.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.fecha_nacimiento, 2, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.nacionalidad = QComboBox(self.widget_registrar_pacientes)
        self.nacionalidad.addItem("")
        self.nacionalidad.addItem("")
        self.nacionalidad.setObjectName(u"nacionalidad")

        self.gridLayout_2.addWidget(self.nacionalidad, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.widget_registrar_pacientes)
        self.widget_pacientes = QWidget()
        self.widget_pacientes.setObjectName(u"widget_pacientes")
        self.stacked_widget.addWidget(self.widget_pacientes)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.nacionalidad)
        QWidget.setTabOrder(self.nacionalidad, self.line_cedula)
        QWidget.setTabOrder(self.line_cedula, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apellido)
        QWidget.setTabOrder(self.line_apellido, self.fecha_nacimiento)
        QWidget.setTabOrder(self.fecha_nacimiento, self.line_telefono)
        QWidget.setTabOrder(self.line_telefono, self.text_direccion)
        QWidget.setTabOrder(self.text_direccion, self.boton_registrar)
        QWidget.setTabOrder(self.boton_registrar, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CITAS", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PACIENTES", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"PACIENTES", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.LOGO.setText("")
        self.line_apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDOS", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRES", None))
        self.boton_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.line_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.text_direccion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N", None))
        self.line_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.nacionalidad.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.nacionalidad.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

    # retranslateUi

