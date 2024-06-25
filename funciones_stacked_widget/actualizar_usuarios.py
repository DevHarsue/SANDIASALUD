from bd.tablas import TablaUsuarios
from validaciones.validaciones_textos import Validador
from validaciones.hash import convertir_texto_hash
from PySide6.QtWidgets import QMessageBox

class VistaActualizarUsuarios:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_usuario.pressed.connect(self.buscar_usuario)
        self.ui.line_usuario.textChanged.connect(self.reiniciar)
        self.ui.boton_actualizar_usuario.pressed.connect(self.actualizar)
        self.ui.boton_borrar_usuario.pressed.connect(self.borrar)
        self.usuario = False
        
    def buscar_usuario(self):
        tabla = TablaUsuarios()
        self.usuario = convertir_texto_hash(self.ui.line_usuario.text())
        self.usuario = tabla.select_usuario(self.usuario)
        if not bool(self.usuario):
            self.usuario = False
            self.ventana.mostrar_mensajes("Usuario No encontrado","No se ha encontrado al usuario")
            return 0

        rol = self.usuario[0][-1]
        if rol == convertir_texto_hash("SUPER-ADMIN"+"\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94"):
            if self.ventana.rol != "SUPER-ADMIN":
                self.ventana.mostrar_mensajes("Acceso Denegado","No tienes permiso para cambiar esta contraseña")
                return 0
            
        self.ui.line_contrasena.setDisabled(False)
        self.ui.line_confirmar.setDisabled(False)
        self.ui.boton_actualizar_usuario.setDisabled(False)
        self.ui.boton_borrar_usuario.setDisabled(False)
    
    def actualizar(self):
        contraseña = self.ui.line_contrasena.text()
        confirmacion = self.ui.line_confirmar.text()
        
        if not Validador().comprobar_contraseña(contraseña):
            self.ventana.mostrar_mensajes("Contraseña Invalida","La contraseña debe contener al menos una letra mayuscula, una minuscula, 2 numeros y un caracter especial")
            return 0
        if contraseña!=confirmacion:
            self.ventana.mostrar_mensajes("Contraseña Invalida","La contraseñas no coinciden")
            return 0
        
        TablaUsuarios().update(str(self.usuario[0][0]),{"contraseña_usuario":convertir_texto_hash(contraseña)})
        # +"\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94"
        
        self.ventana.mostrar_mensajes("Usuario Actualizado","Contraseña Cambiada Satisfactoriamente")
        self.reiniciar()

    def borrar(self):
        if str(self.usuario[0][0]) == str(self.ventana.id):
            self.ventana.mostrar_mensajes("Acceso Denegado","No puedes eliminar el usuario con el que iniciaste sesion")
            return 0
        respuesta = self.ventana.preguntar("Borrar Usuario","¿Estas seguro de eliminar este usuario?")
        if respuesta == QMessageBox.StandardButton.No:
            return 0
        TablaUsuarios().delete(str(self.usuario[0][0]))
        self.reiniciar()
        
    def reiniciar(self):
        self.ui.line_contrasena.setDisabled(True)
        self.ui.line_confirmar.setDisabled(True)
        self.ui.line_contrasena.setText("")
        self.ui.line_confirmar.setText("")
        self.ui.boton_actualizar_usuario.setDisabled(True)
        self.ui.boton_borrar_usuario.setDisabled(True)
        self.usuario = False