from bd.tablas import TablaPacientes,TablaAntecedentes,TablaEmbarazos,TablaCitas,TablaConsultas
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QPropertyAnimation,QEasingCurve,QDate
from validaciones.validaciones_textos import Validador
from obtener_fecha import obtener_fecha
from pdf.consulta import Consulta
import os
import webbrowser


class VistaConsulta:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.antecedente = False
        self.preparar()
    
    def preparar(self):
        self.validador = Validador()
        self.validador.cedulas(self.ui.line_consulta_cedula)
        self.ui.boton_consulta_cedula.pressed.connect(self.buscar_paciente)
        self.ui.boton_ver_antecedentes.pressed.connect(self.mostrar_antecedentes)
        
        self.ui.combo_consulta_antecedentes.currentIndexChanged.connect(self.reiniciar_paciente)
        self.ui.line_consulta_cedula.textChanged.connect(self.reiniciar_paciente)
        
        self.ui.check_proxima_cita_consulta.stateChanged.connect(self.agendar_cita)
        self.ui.check_embarazo_consulta.stateChanged.connect(self.embarazo)
        
        self.ui.boton_fin_consulta.pressed.connect(self.fin_consulta)
        self.cita_id = False
        self.reiniciar_paciente()
    
    def buscar_paciente(self):
        tabla_paciente = TablaPacientes()
        nacionalidad = self.ui.combo_consulta_antecedentes.currentText()
        cedula = self.ui.line_consulta_cedula.text()
        
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
                self.ui.nacionalidad.setCurrentIndex(self.ui.combo_consulta_antecedentes.currentIndex())
            return 0
        
        self.paciente = self.paciente[0]
        tabla_citas = TablaCitas()
        cita = tabla_citas.select_citas_paciente(self.paciente[0])
        if not bool(cita):
            respuesta = self.ventana.preguntar("El cliente no tiene cita previa","¿Desea realizar consulta sin cita previa?")
            if respuesta == QMessageBox.StandardButton.No:
                return 0
            self.fecha = obtener_fecha()
            self.cita_id = False
        else:
            self.fecha = cita[0][1].strftime('%Y-%m-%d %H:%M:%S')
            self.cita_id = cita[0][0]
        
        self.ui.line_consulta_nombre.setText(self.paciente[3])
        self.ui.line_consulta_apellido.setText(self.paciente[4])
        embarazo = TablaEmbarazos().select_citas_paciente(str(self.paciente[0]))
        if bool(embarazo):
            embarazo = embarazo[0]
            regla = embarazo[1]
            año = int(regla.strftime("%Y"))
            mes = int(regla.strftime("%m"))
            dia = int(regla.strftime("%d"))
            self.ui.date_consulta_ultima_regla.setDate(QDate(año,mes,dia))
            parto = embarazo[2]
            año = int(parto.strftime("%Y"))
            mes = int(parto.strftime("%m"))
            dia = int(parto.strftime("%d"))
            self.ui.date_consulta_parto.setDate(QDate(año,mes,dia))


    def reiniciar_paciente(self):
        self.ui.line_consulta_nombre.setText("")
        self.ui.line_consulta_apellido.setText("")
        self.ui.text_antecedente_patologico.setText("")
        self.ui.text_antecedentes_quirurjicos.setText("")
        self.ui.text_tratamiento_actual.setText("")
        self.ui.date_primera_relacion_consulta.setDate(QDate(2024,1,1))
        self.ui.date_proxima_cita_consulta.setDate(QDate(2024,1,1))
        self.ui.date_consulta_ultima_regla.setDate(QDate(2024,1,1))
        self.ui.date_consulta_parto.setDate(QDate(2024,1,1))
        self.ui.check_proxima_cita_consulta.setChecked(False)
        self.ui.check_embarazo_consulta.setChecked(False)
        self.antecedente = False
        
        self.animacion_antecedentes(False)
    
    def mostrar_antecedentes(self):
        if self.ui.line_consulta_nombre.text()=="":
            self.ventana.mostrar_mensajes("Paciente no seleccionado","Seleccione un paciente")
            return 0;
        
        tabla = TablaAntecedentes()
        self.antecedente = tabla.select_antecedente_paciente(self.paciente[0])
        if not bool(self.antecedente):
            self.ventana.mostrar_mensajes("Antecedentes No Encontrados","No se han encontrado antecedentes para el paciente")
            respuesta = self.ventana.preguntar("Registar Antecedentes","¿Desea Registrar Antecedentes para el Paciente?")
            if respuesta == QMessageBox.StandardButton.Yes:
                self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_antecedente)
            return 0
        
        self.antecedente = self.antecedente[0]
        self.ui.text_antecedente_patologico.setText(self.antecedente[1])
        self.ui.text_antecedentes_quirurjicos.setText(self.antecedente[2])
        self.ui.text_tratamiento_actual.setText(self.antecedente[3])
        año = int(self.antecedente[4].strftime("%Y"))
        mes = int(self.antecedente[4].strftime("%m"))
        dia = int(self.antecedente[4].strftime("%d"))
        self.ui.date_primera_relacion_consulta.setDate(QDate(año,mes,dia))
        
        if self.ui.consulta_antecedentes.height()==0:
            self.animacion_antecedentes(True)
        else:
            self.animacion_antecedentes(False)
            self.antecedente = False
            
        
    def animacion_antecedentes(self,estado):
        self.animation = QPropertyAnimation(self.ui.consulta_antecedentes, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setEndValue(400 if estado else 0)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()
        
    def agendar_cita(self):
        if self.ui.check_proxima_cita_consulta.isChecked():
            self.ui.date_proxima_cita_consulta.setDisabled(False)
        else:
            self.ui.date_proxima_cita_consulta.setDisabled(True)
    
    def embarazo(self):
        if self.ui.check_embarazo_consulta.isChecked():
            self.ui.date_consulta_ultima_regla.setDisabled(False)
            self.ui.date_consulta_parto.setDisabled(False)
        else:
            self.ui.date_consulta_ultima_regla.setDisabled(True)
            self.ui.date_consulta_parto.setDisabled(True)
    
    def fin_consulta(self):
        if self.ui.line_consulta_nombre.text()=="":
            self.ventana.mostrar_mensajes("Sin Paciente","Seleccione un Paciente.")
            return 0
        
        diagnostico = self.ui.text_consulta_diagnostico.toPlainText()
        tratamiento = self.ui.text_consulta_tratamiento.toPlainText()
        
        if diagnostico=="":
            respuesta = self.ventana.preguntar("No hay diagnostico","No hay diagnostico, ¿Registrar de todos modos?")
            if respuesta == QMessageBox.StandardButton.No:
                return 0
        if tratamiento=="":
            respuesta = self.ventana.preguntar("No hay tratamiento","No hay tratamiento, ¿Registrar de todos modos?")
            if respuesta == QMessageBox.StandardButton.No:
                return 0
            
        if bool(self.antecedente):
            respuesta = self.ventana.preguntar("Actualizacion de Antecedentes","Se van a actualizar los antecedentes, ¿Estas de acuerdo?") 
            if respuesta == QMessageBox.StandardButton.Yes:
                patologico = self.ui.text_antecedente_patologico.toPlainText()
                quirurjico = self.ui.text_antecedentes_quirurjicos.toPlainText()
                tratamiento = self.ui.text_tratamiento_actual.toPlainText()
                relacion = self.ui.date_primera_relacion_consulta.date().toString("yyyy-MM-dd")
                tabla = TablaAntecedentes()
                tabla.update(self.antecedente[0],{"antecedentes_patologicos":patologico,"antecedentes_quirurjicos":quirurjico,"tratamiento_actual":tratamiento,"fecha_primera_relacion_sexual":relacion})
                
        if self.ui.check_proxima_cita_consulta.isChecked():
            tabla = TablaCitas()
            self.fecha_proxima = self.ui.date_proxima_cita_consulta.dateTime().toString("yyyy-MM-dd hh:mm")
            cita = tabla.select_citas_paciente(self.paciente[0])
            if not bool(cita):
                tabla.insert(self.fecha_proxima,str(self.paciente[0]))
            else:
                tabla.update(cita[0][0],{"fecha_proxima_cita":self.fecha_proxima})
        else:
            self.fecha_proxima = False
                
        if self.ui.check_embarazo_consulta.isChecked():
            tabla = TablaEmbarazos()
            self.regla = self.ui.date_consulta_ultima_regla.date().toString("yyyy-MM-dd")
            self.parto = self.ui.date_consulta_parto.date().toString("yyyy-MM-dd")
            embarazo = tabla.select_citas_paciente(self.paciente[0])
            if not bool(embarazo):
                tabla.insert(self.regla,self.parto,str(self.paciente[0]))
            else:
                tabla.update(embarazo[0][0],{"fecha_ultima_regla":self.regla,"fecha_probable_parto":self.parto})
        else:
            self.regla = False
            self.parto = False
        
        tabla = TablaConsultas()
        tabla.insert(str(self.paciente[0]),diagnostico,tratamiento,self.fecha)
        
        if not self.ui.check_proxima_cita_consulta.isChecked() and self.cita_id:
            TablaCitas().delete(str(self.cita_id))
            
        self.ventana.mostrar_mensajes("Consulta finalizada","Consulta realizada existosamente")
        
        id = tabla.select_consultas_paciente(str(self.paciente[0]))[0][0]
        pdf = Consulta(id,self.paciente[1],self.paciente[2],self.paciente[3],self.paciente[4],diagnostico,tratamiento,self.fecha,self.fecha_proxima,self.regla,self.parto)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\SANDIASALUD")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\SANDIASALUD\\Consulta_{self.paciente[3]}_{self.paciente[4]}_{id}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        
        self.reiniciar_paciente()
        self.reiniciar()
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_inicio)
        
    
    def reiniciar(self):
        self.ui.line_consulta_cedula.setText("")
        self.ui.combo_consulta_antecedentes.setCurrentIndex(0)
        self.ui.text_consulta_diagnostico.setText("")
        self.ui.text_consulta_tratamiento.setText("")
