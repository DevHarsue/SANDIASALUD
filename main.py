from interfaz.interfaz_principal import Ui_SANDIASALUD
from interfaz.interfaz_inicio import Ui_Login
from bd.comprobar_bd import ComprobadorBD
from funciones_stacked_widget.registrar_pacientes import VistaRegistrarPacientes
from funciones_stacked_widget.agendar_cita import VistaAgendarCita
from funciones_stacked_widget.citas import VistaCitas
from funciones_stacked_widget.consulta import VistaConsulta
from funciones_stacked_widget.antecedentes import VistaAntecedentes
from funciones_stacked_widget.pacientes import VistaPacientes
from funciones_stacked_widget.consultas import VistaConsultas
from funciones_stacked_widget.configuracion import VistaConfiguracion
from funciones_stacked_widget.actualizar_usuarios import VistaActualizarUsuarios
from validaciones.hash import convertir_texto_hash
from bd.tablas import TablaUsuarios
from ventanas import VentanaConfiguracion,VentanaUsuarios
from PySide6.QtWidgets import QMainWindow, QApplication,QMessageBox
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self,rol,ventana,id):
        super().__init__()
        self.rol = rol
        self.ventana = ventana
        self.id = id
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
        self.vista_consultas = VistaConsultas(self)
        self.vista_configuracion = VistaConfiguracion(self)
        self.vista_actualizar_usuarios = VistaActualizarUsuarios(self)
    
    def asignar_slots_vistas(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio)
        self.ui.boton_inicio.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio))
        self.ui.boton_v_agendar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_agendar_cita))
        self.ui.boton_v_citas.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_citas))
        self.ui.boton_v_consulta.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_consulta))
        self.ui.boton_v_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_pacientes))
        self.ui.boton_v_registrar_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_pacientes))
        self.ui.boton_v_consultas.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_consultas))
        self.ui.boton_v_configuracion.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_configuracion))
        self.ui.boton_v_actulizar_usuarios.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_actualizar_usuarios))
        self.ui.boton_v_cerrar_sesion.pressed.connect(self.cerrar_sesion)
        
    def ajustar_ventana(self):
        if self.rol == "USUARIO":
            self.ui.boton_v_consulta.hide()
            self.ui.contenedor_consulta.hide()
            self.ui.contenedor_antecedentes.hide()
            self.ui.contenedor_datos_embarazo.hide()
            self.ui.boton_v_configuracion.hide()
            self.ui.boton_v_consultas.hide()
            self.ui.boton_borrar_paciente.hide()
            self.ui.boton_imprimir.hide()
        elif self.rol == "ADMIN":
            self.ui.boton_configurar_bd.hide()
    
    def cerrar_sesion(self):
        respuesta = self.preguntar("Cerrar Sesion","¿Estas seguro que deseas cerrar sesion?")
        if respuesta == QMessageBox.StandardButton.No:
            return 0
        self.close()
        self.ventana.show()
        self.deleteLater()

    
    def mostrar_mensajes(self,titulo,texto):
        QMessageBox.information(self,titulo,texto,QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
    def preguntar(self,titulo,texto):
        return QMessageBox.question(self,titulo,texto,QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        
class VentanaIniciarSesion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.boton_iniciar.pressed.connect(self.validar_inicio)
        self.show()
        if not ComprobadorBD().comprobar():
            self.cambiar_ventana_configuracion()
        else:
            roles = TablaUsuarios().select_rol()
            if not tuple(filter(lambda x: x[0]==convertir_texto_hash("SUPER-ADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),roles)):
                self.close()
                self.ventana_configurar_usuarios = VentanaUsuarios(self)
                self.ventana_configurar_usuarios.show()
                
        

    
    def validar_inicio(self):
        tabla_usuarios = TablaUsuarios()
        usuario = tabla_usuarios.select_usuario(convertir_texto_hash(self.ui.line_usuario.text()))
        if not bool(usuario):
            QMessageBox.information(self,"No existe el usuario","El usuario no existe",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        contraseña = usuario[0][2]
        contraseña_introducida = convertir_texto_hash(self.ui.line_contrasena.text())
        
        #Borrar esto
        # if contraseña_introducida==convertir_texto_hash(""):
        #     self.cambiar_ventana("SUPER-ADMIN",usuario[0][0])
        #     return 0
        
        if contraseña!=contraseña_introducida:
            QMessageBox.information(self,"Contraseña Incorrecta","La contraseña no coincide",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        salt = '\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'
        rol = "SUPER-ADMIN" if convertir_texto_hash("SUPER-ADMIN"+salt) == usuario[0][-1] else "ADMIN" if convertir_texto_hash("ADMIN"+salt) == usuario[0][-1] else "USUARIO"
        self.cambiar_ventana(rol,usuario[0][0])
        self.ui.line_contrasena.setText("")
        self.ui.line_usuario.setText("")
        
    def cambiar_ventana(self,rol,id):
        self.close()
        self.venta_principal = VentanaPrincipal(rol,self,id)
        self.venta_principal.show()

    def cambiar_ventana_configuracion(self):
        self.close()
        self.ventana_configuracion = VentanaConfiguracion(self)
        self.ventana_configuracion.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaIniciarSesion()
    sys.exit(app.exec())