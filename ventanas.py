from interfaz.interfaz_configuracion import Ui_Configuracion
from interfaz.interfaz_usuarios import Ui_Usuarios
from bd.comprobar_bd import ComprobadorBD
from validaciones.hash import convertir_texto_hash
from bd.tablas import TablaUsuarios
from validaciones.validaciones_textos import Validador
from PySide6.QtWidgets import QMainWindow, QMessageBox

class VentanaConfiguracion(QMainWindow):
    def __init__(self,ventana) -> None:
        super().__init__()
        self.ventana = ventana
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.ui.boton_iniciar.pressed.connect(self.conectar)
        self.ui.boton_volver.pressed.connect(self.volver)
        
    def conectar(self):
        user = self.ui.line_usuario.text()
        password = self.ui.line_contrasena.text()
        host = self.ui.line_host.text()
        puerto = self.ui.line_puerto.text()
        if not ComprobadorBD().testear(user,password,host,puerto):
            QMessageBox.information(self,"Error de conexion","Comprueba los datos para conectar a la base de datos.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        if not ComprobadorBD().crear_env(user,password,host,puerto):
            QMessageBox.information(self,"Error de configuración","No se pudo crear el archivo env",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        QMessageBox.information(self,"Conexion establecida","Conexion a la base de datos realizada correctamente.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        
        roles = TablaUsuarios().select_rol()
        if not tuple(filter(lambda x: x[0]==convertir_texto_hash("SUPER-ADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),roles)):
            self.close()
            self.ventana_configurar_usuarios = VentanaUsuarios(self.ventana)
            self.ventana_configurar_usuarios.show()
            return 0

            
        self.close()
        self.ventana.show()
        
    def volver(self):
        self.close()
        self.ventana.show()

class VentanaUsuarios(QMainWindow):
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        super().__init__()
        self.ui = Ui_Usuarios()
        self.ui.setupUi(self)
        self.ui.boton_registrar.pressed.connect(self.guardar_usuarios)
        Validador().usuarios(self.ui.line_usuario)
        self.ui.boton_volver.pressed.connect(self.volver)
    
    def guardar_usuarios(self):
        usuario = self.ui.line_usuario.text()
        if usuario=="":
            QMessageBox.information(self,"Error de registro","El campo usuario no puede estar vacío.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        if bool(TablaUsuarios().select_usuario(convertir_texto_hash(usuario))):
            QMessageBox.information(self,"Error de registro","El usuario ya existe.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        contraseña = self.ui.line_contrasena.text()
        if not Validador().comprobar_contraseña(contraseña):
            QMessageBox.information(self,"Contraseña Invalida","La contraseña debe contener al menos una letra mayuscula, una minuscula, 2 numeros y un caracter especial",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0

        confirmacion= self.ui.line_confirmacion.text()
        if contraseña!=confirmacion:
            QMessageBox.information(self,"Contraseña Invalida","La contraseñas no coinciden",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        rol = self.ui.combo_tipo.currentText()
        
        usuario = convertir_texto_hash(usuario)
        contraseña = convertir_texto_hash(contraseña)
        rol_hash = convertir_texto_hash(rol+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94')
        TablaUsuarios().insert(usuario,contraseña,rol_hash)
        QMessageBox.information(self,"Registro Exitoso",f"Usuario {rol}, registrado correctamente")
        if rol !="SUPER-ADMIN":
            existe_super = tuple(filter(lambda x: x[0]==convertir_texto_hash("SUPER-ADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),TablaUsuarios().select_rol()))
            if not bool(existe_super):
                QMessageBox.information(self,"Falta SUPER-ADMIN","No hay un SUPER-ADMIN registrado\n Porfavor registre uno",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.reiniciar()
                return 0
        else:
            self.ui.combo_tipo.removeItem(0)
        
        respuesta = QMessageBox.question(self,"Registrar mas usuarios","¿Desea Registrar mas usuarios?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self.reiniciar()
            return 0
        
        self.close()
        self.ventana.show()

    def reiniciar(self):
        self.ui.combo_tipo.setCurrentIndex(0)
        self.ui.line_usuario.setText("")
        self.ui.line_confirmacion.setText("")
        self.ui.line_contrasena.setText("")
        
    def volver(self):
        self.close()
        self.ventana.show()