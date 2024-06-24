from bd.tablas import TablaAntecedentes
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMessageBox


class VistaAntecedentes:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_registrar_antecedentes.pressed.connect(self.registrar_antecedente)
        self.ui.date_primera_relacion.setDate(QDate(2024,1,1))
        
    def registrar_antecedente(self):
        tabla = TablaAntecedentes()
        antecedente_patologico = self.ui.text_antecedente_patologico_registro.toPlainText()
        antecedente_quirurjico = self.ui.text_antecedente_quirurjico_registro.toPlainText()
        tratamiento_actual = self.ui.text_tratamiento_registro.toPlainText()
        fecha_relaciones = self.ui.date_primera_relacion.date().toString("yyyy-MM-dd")
        
        if antecedente_patologico=="" or antecedente_quirurjico=="" or tratamiento_actual=="":
            respuesta = self.ventana.preguntar("Datos Faltantes","Faltan algunos datos, ¿Deseas registrar los antecedentes igualmente?") 
            if respuesta == QMessageBox.StandardButton.No:
                return 0
        
        tabla.insert(antecedente_patologico,antecedente_quirurjico,tratamiento_actual,fecha_relaciones,str(self.ventana.vista_consulta.paciente[0]))
        self.ventana.mostrar_mensajes("Antecedentes Registrados","Los Antecedentes del paciente han sido registrados correctamente")
        
        self.reiniciar()
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_consulta)
        self.ventana.vista_consulta.mostrar_antecedentes()
    
    def reiniciar(self):
        self.ui.text_antecedente_patologico_registro.setText("")
        self.ui.text_antecedente_quirurjico_registro.setText("")
        self.ui.text_tratamiento_registro.setText("")
        self.ui.date_primera_relacion.setDate(QDate(2024,1,1))
        