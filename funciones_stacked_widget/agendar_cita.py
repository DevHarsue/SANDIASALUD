from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QMessageBox
from bd.tablas import TablaPacientes,TablaCitas
from validaciones.validaciones_textos import Validador

class VistaAgendarCita:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.preparar()
        self.ui.boton_buscar_agenda.pressed.connect(self.buscar_paciente)
        self.ui.boton_agendar.pressed.connect(self.validar_agenda)
    
    def preparar(self):
        self.validador = Validador()
        self.validador.cedulas(self.ui.line_cedula_agenda)
        self.ui.date_agenda.setDateTime(QDateTime(2024,1,1,14,0,0))
        self.ui.combo_nacionalidad_agenda.currentIndexChanged.connect(self.reiniciar_paciente)
        self.ui.line_cedula_agenda.textChanged.connect(self.reiniciar_paciente)
    
    def reiniciar_paciente(self):
        self.ui.line_nombre_agenda.setText("")
        self.ui.line_apellido_agenda.setText("")
    
    def buscar_paciente(self):
        self.ui.stacked_widget
        tabla_paciente = TablaPacientes()
        nacionalidad = self.ui.combo_nacionalidad_agenda.currentText()
        cedula = self.ui.line_cedula_agenda.text()
        
        if cedula==""or len(cedula)<7 or len(cedula)>9:
            self.ventana.mostrar_mensajes("Cedula no valida","Ingresa una cedula valida.")
            return 0
        
        self.paciente = tabla_paciente.select_cedula(nacionalidad,cedula)
        if not self.paciente:
            self.ventana.mostrar_mensajes("Paciente no encontrado","Paciente no registrado")
            respuesta = self.ventana.preguntar("Registar Paciente","¿Desea Registrar un nuevo paciente?")
            if respuesta == QMessageBox.StandardButton.Yes:
                self.ventana.vista_registrar_pacientes.index=self.ui.stacked_widget.currentIndex()
                self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_pacientes)
                self.ui.line_cedula.setText(cedula)
                self.ui.nacionalidad.setCurrentIndex(self.ui.combo_nacionalidad_agenda.currentIndex())
                return 0
        else:
            self.paciente = self.paciente[0]
            self.ui.line_nombre_agenda.setText(self.paciente[3])
            self.ui.line_apellido_agenda.setText(self.paciente[4])
    
    def validar_agenda(self):
        if self.ui.line_nombre_agenda.text()=="":
            self.ventana.mostrar_mensajes("Busca el Paciente","Introduce una cedula y presiona buscar.")
            return 0
        fecha =self.ui.date_agenda.dateTime().toString("yyyy-MM-dd hh-mm-ss")
        tabla_cita = TablaCitas()
        cita = tabla_cita.select_citas_paciente(self.paciente[0])
        if not cita:
            tabla_cita.insert(fecha,str(self.paciente[0]))
        else:
            tabla_cita.update(cita[0][0],{"fecha_proxima_cita":fecha})
            
        self.ventana.mostrar_mensajes("Cita Agendada","La cita ha sido agendada existosamente")
        self.reiniciar()
    
    def reiniciar(self):
        self.ui.line_cedula_agenda.setText("")
        self.ui.combo_nacionalidad_agenda.setCurrentIndex(0)
        self.ui.date_agenda.setDateTime(QDateTime(2024,1,1,14,0,0))
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio)