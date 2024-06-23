from interfaz.interfaz_principal import Ui_SANDIASALUD
from interfaz.interfaz_inicio import Ui_Login
from funciones_stacked_widget.registrar_pacientes import VistaRegistrarPacientes
from funciones_stacked_widget.agendar_cita import VistaAgendarCita
from funciones_stacked_widget.citas import VistaCitas
from funciones_stacked_widget.consulta import VistaConsulta
from funciones_stacked_widget.antecedentes import VistaAntecedentes
from funciones_stacked_widget.pacientes import VistaPacientes
from validaciones.hash import convertir_texto_hash
from bd.tablas import TablaUsuarios

from PySide6.QtWidgets import QMainWindow, QApplication,QMessageBox,QLineEdit
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self,permisos):
        super().__init__()
        self.permisos = permisos
        self.ui = Ui_SANDIASALUD()
        self.ui.setupUi(self)
        self.asignar_slots_vistas()
        self.ajustar_ventana()
        self.vista_registrar_pacientes = VistaRegistrarPacientes(self)
        self.vista_cita = VistaCitas(self)
        self.vista_agendar_cita = VistaAgendarCita(self)
        self.vista_consulta = VistaConsulta(self)
        self.vista_antecedentes = VistaAntecedentes(self)
        self.vista_pacientes = VistaPacientes(self)
        
    
    def asignar_slots_vistas(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio)
        self.ui.boton_inicio.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio))
        self.ui.boton_v_agendar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_agendar_cita))
        self.ui.boton_v_citas.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_citas))
        self.ui.boton_v_consulta.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_consulta))
        self.ui.boton_v_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_pacientes))
        self.ui.boton_v_registrar_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_pacientes))
    def ajustar_ventana(self):
        if not self.permisos[0]:
            self.ui.boton_v_consulta.hide()
        if not self.permisos[1]:
            self.ui.contenedor_consulta.hide()
        if not self.permisos[2]:
            self.ui.contenedor_antecedentes.hide()
        if not self.permisos[3]:
            self.ui.contenedor_datos_embarazo.hide()
        if not self.permisos[4]:
            self.ui.boton_v_configuracion.hide()
        if not self.permisos[5]:
            pass
            self.ui.boton_registrar_usuarios.hide()
    
    def mostrar_mensajes(self,titulo,texto):
        QMessageBox.information(self,titulo,texto,QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
    def preguntar(self,titulo,texto):
        return QMessageBox.question(self,titulo,texto,QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        
class VentanaIniciarSesion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.line_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.boton_iniciar.pressed.connect(self.validar_inicio)
        self.show()
    
    def validar_inicio(self):
        tabla_usuarios = TablaUsuarios()
        usuario = tabla_usuarios.select_usuario(self.ui.line_usuario.text())
        if not bool(usuario):
            QMessageBox.information(self,"No existe el usuario","El usuario no existe",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        contraseña = usuario[0][2]
        contraseña_introducida = convertir_texto_hash(self.ui.line_contrasena.text())
        
        if contraseña_introducida==convertir_texto_hash(""):
            self.cambiar_ventana(usuario[0][3:])
            return 0
        
        if contraseña!=contraseña_introducida:
            QMessageBox.information(self,"Contraseña Incorrecta","La contraseña no coincide",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        self.cambiar_ventana(usuario[0][3:])
        
    def cambiar_ventana(self,permisos):
        self.close()
        self.venta_principal = VentanaPrincipal(permisos)
        self.venta_principal.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaIniciarSesion()
    sys.exit(app.exec())