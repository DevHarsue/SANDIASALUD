# from main import VentanaPrincipal
from bd.tablas import TablaPacientes,TablaConsultas
from validaciones.validaciones_textos import Validador
from PySide6.QtWidgets import QMessageBox,QTableWidgetItem

class VistaConsultas:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.paciente = False
        self.id = False
        self.preparar()
    
    def preparar(self):
        validador = Validador()
        validador.cedulas(self.ui.line_cedula_consultas)
        self.ui.boton_buscar_consultas.clicked.connect(self.buscar_paciente)
        self.ui.table_consultas.currentCellChanged.connect(self.agregar_consulta)
        self.ui.line_cedula_consultas.textChanged.connect(self.reiniciar)
        self.ui.check_editar_consultas.stateChanged.connect(self.cambiar_actualizar)
        self.ui.boton_borrar_consultas.pressed.connect(self.eliminar)
        self.ui.boton_actualizar_consultas.pressed.connect(self.actualizar)
    
    def buscar_paciente(self):
        self.reiniciar()
        nacionalidad = self.ui.combo_nacionalidad_consultas.currentText()
        cedula = self.ui.line_cedula_consultas.text()
        
        if cedula==""or len(cedula)<7 or len(cedula)>9:
            self.ventana.mostrar_mensajes("Cedula no valida","Ingresa una cedula valida.")
            return 0
        
        tabla = TablaPacientes()
        self.paciente = tabla.select_cedula(nacionalidad,cedula)

        if not self.paciente:
            self.ventana.mostrar_mensajes("Paciente no encontrado","Paciente no registrado")
            respuesta = self.ventana.preguntar("Registar Paciente","¿Desea Registrar un nuevo paciente?")
            if respuesta == QMessageBox.StandardButton.Yes:
                self.ventana.vista_registrar_pacientes.index=self.ui.stacked_widget.currentIndex()
                self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_pacientes)
                self.ui.line_cedula.setText(cedula)
                self.ui.nacionalidad.setCurrentIndex(self.ui.combo_nacionalidad_consultas.currentIndex())
                
            return 0

        tabla = TablaConsultas()
        consultas = tabla.select_todas_consultas_paciente(str(self.paciente[0][0]))
        if not bool(consultas):
            return 0

        
        for i,consulta in enumerate(consultas):
            self.ui.table_consultas.insertRow(self.ui.table_consultas.rowCount())
            self.ui.table_consultas.setItem(i,0,QTableWidgetItem(str(consulta[0])))
            self.ui.table_consultas.setItem(i,1,QTableWidgetItem(str(self.paciente[0][3])))
            self.ui.table_consultas.setItem(i,2,QTableWidgetItem(str(self.paciente[0][4])))
            self.ui.table_consultas.setItem(i,3,QTableWidgetItem(str(consulta[-1])))
    
        
        
    def agregar_consulta(self,row):
        self.id = self.ui.table_consultas.item(row,0)
        if not self.id:
            self.id = False
            return 0    
        self.id = self.id.text()
        consulta = TablaConsultas().select(int(self.id))[0]
        self.ui.text_diagnostico_edit.setText(consulta[2])
        self.ui.text_tratamiento_edit.setText(consulta[3])
        self.ui.boton_borrar_consultas.setDisabled(False)
        self.ui.check_editar_consultas.setDisabled(False)

    def reiniciar(self):
        while self.ui.table_consultas.rowCount() > 0:
            self.ui.table_consultas.removeRow(0)
        self.ui.check_editar_consultas.setDisabled(True)
        self.ui.check_editar_consultas.setChecked(False)
        self.ui.text_diagnostico_edit.setText("")
        self.ui.text_tratamiento_edit.setText("")
        self.ui.boton_actualizar_consultas.setDisabled(True)
        self.ui.boton_borrar_consultas.setDisabled(True)
        self.id = False
        
    def cambiar_actualizar(self,estado):
        if estado:
            self.ui.boton_actualizar_consultas.setDisabled(False)
            self.ui.text_diagnostico_edit.setDisabled(False)
            self.ui.text_tratamiento_edit.setDisabled(False)
        else:
            self.ui.boton_actualizar_consultas.setDisabled(True)
            self.agregar_consulta(self.ui.table_consultas.currentRow())
            self.ui.text_diagnostico_edit.setDisabled(True)
            self.ui.text_tratamiento_edit.setDisabled(True)

    def eliminar(self):
        respuesta = self.ventana.preguntar("Eliminar Consulta","¿Estas seguro de eliminar la consulta?")
        if respuesta == QMessageBox.StandardButton.Yes:
            TablaConsultas().delete(int(self.id))
            self.ventana.mostrar_mensajes("Consulta Borrada Exitosamente","La consulta ha sido borrada exitosamente")
            self.reiniciar()
            self.buscar_paciente()
    
    def actualizar(self):
        respuesta = self.ventana.preguntar("Actualizar Consulta","¿Estas seguro de actualizar la consulta?")
        if respuesta == QMessageBox.StandardButton.Yes:
            tratamiento = self.ui.text_tratamiento_edit.toPlainText()
            diagnostico = self.ui.text_diagnostico_edit.toPlainText()
            TablaConsultas().update(int(self.id),{"diagnostico":diagnostico,"tratamiento":tratamiento})
            self.ventana.mostrar_mensajes("Consulta Actualizada Exitosamente","La consulta ha sido actualizada exitosamente")
            self.reiniciar()
            self.buscar_paciente()