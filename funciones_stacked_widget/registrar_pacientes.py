from PySide6.QtCore import QDate
from bd.tablas import TablaPacientes
from validaciones.validaciones_textos import Validador

class VistaRegistrarPacientes:
    def __init__(self,ventana):
        self.ventana= ventana
        self.ui = ventana.ui
        self.tabla = TablaPacientes()
        self.index = -1
        self.ui.boton_registrar.pressed.connect(self.validar_paciente)
        self.preparar()
        self.agregar_validaciones_line()
    
    def preparar(self):
        self.ui.fecha_nacimiento.setDate(QDate(2024,1,1))
    
    def agregar_validaciones_line(self):
        validador = Validador()
        validador.cedulas(self.ui.line_cedula)
        validador.solo_texto(self.ui.line_nombre)
        validador.solo_texto(self.ui.line_apellido)
        validador.numero_telefono(self.ui.line_telefono)
    
    def validar_paciente(self):
        nacionalidad = self.ui.nacionalidad.currentText()
        cedula = self.ui.line_cedula.text()
        nombre = self.ui.line_nombre.text()
        apellido = self.ui.line_apellido.text()
        fecha = self.ui.fecha_nacimiento.date().toString("yyyy-MM-dd")
        telefono = self.ui.line_telefono.text()
        direccion = self.ui.text_direccion.toPlainText()
        
        if bool(self.tabla.select_cedula(nacionalidad,cedula)):
            self.ventana.mostrar_mensajes("Paciente ya registrado","Este paciente ya ha sido registrado antes.")
            return 0
            
        if cedula =="" or len(cedula)<7 or len(cedula)>9:
            self.ventana.mostrar_mensajes("Cedula incorrecta","La cedula debe contener minimo 7 caracteres y maximo 9 caracteres")
            return 0
        if nombre=="" or apellido=="":
            self.ventana.mostrar_mensajes("Nombre o Apellido incorrecto","El nombre y apellido son obligatorios")
            return 0
        if telefono=="" or len(telefono)<10:
            self.ventana.mostrar_mensajes("Telefono erroneo","El telefono debe ser de minimo 10 digitos")
            return 0
        
        self.tabla.insert(nacionalidad,cedula,nombre,apellido,fecha,telefono,direccion)
        self.ui.stacked_widget.setCurrentIndex(self.index if self.index!=-1 else 2)
        self.ventana.mostrar_mensajes("REGISTRO EXISTOSO","Paciente registrado exitosamente.")
        self.reiniciar_datos()
        self.index = -1
    
    def reiniciar_datos(self):
        self.ui.line_cedula.setText("")
        self.ui.line_nombre.setText("")
        self.ui.line_apellido.setText("")
        self.ui.line_telefono.setText("")
        self.ui.text_direccion.setText("")
        self.ui.fecha_nacimiento.setDate(QDate(2024,1,1))
        self.ui.nacionalidad.setCurrentIndex(0)
        
        
        