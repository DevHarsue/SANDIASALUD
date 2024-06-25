from PySide6.QtCore import QDate,QDateTime
from PySide6.QtWidgets import QMessageBox
from bd.tablas import TablaCitas,TablaPacientes,TablaConsultas,TablaEmbarazos,TablaAntecedentes
from validaciones.validaciones_textos import Validador
from pdf.paciente import Paciente
import os
import webbrowser

class VistaPacientes:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.preparar()
        self.paciente = False
    
    def preparar(self):
        if self.ventana.rol=="USUARIO":
            self.ui.contenedor_consulta.hide()
            self.ui.contenedor_antecedentes.hide()
            self.ui.contenedor_datos_embarazo.hide()
        
        self.ui.boton_buscar.pressed.connect(self.buscar_paciente)
        
        self.ui.date_fecha_nacimiento.setDate(QDate(2024,1,1))
        self.ui.date_proxima_cita.setDateTime(QDateTime(2024,1,1,14,0,0))
        self.ui.date_relaciones.setDate(QDate(2024,1,1))
        self.ui.date_ultima_regla.setDate(QDate(2024,1,1))
        self.ui.date_parto.setDate(QDate(2024,1,1))
        
        self.ui.check_datos_personales.stateChanged.connect(self.cambiar_datos_personales)
        self.ui.check_proxima_cita.stateChanged.connect(self.cambiar_proxima_cita)
        self.ui.check_consulta.stateChanged.connect(self.cambiar_consulta)
        self.ui.check_antecedentes.stateChanged.connect(self.cambiar_antecedentes)
        self.ui.check_embarazo.stateChanged.connect(self.cambiar_embarazo)
        
        self.ui.boton_actualizar_datos.pressed.connect(self.actualizar)
        self.ui.line_cedula_buscar.textChanged.connect(self.reiniciar)
        validador = Validador()
        validador.cedulas(self.ui.line_cedula_buscar)
        validador.solo_texto(self.ui.line_nombre_editar)
        validador.solo_texto(self.ui.line_apellido_editar)
        validador.numero_telefono(self.ui.line_telefono_editar)
        
        self.ui.boton_imprimir.pressed.connect(self.imprimir)
        self.ui.boton_borrar_paciente.pressed.connect(self.borrar_paciente)
    
    
    def buscar_paciente(self):
        self.reiniciar()        
        tabla_paciente = TablaPacientes()
        nacionalidad = self.ui.combo_nacionalidad.currentText()
        cedula = self.ui.line_cedula_buscar.text()
        
        if cedula==""or len(cedula)<7 or len(cedula)>9:
            self.ventana.mostrar_mensajes("Cedula no valida","Ingresa una cedula valida.")
            return 0
        
        self.paciente = tabla_paciente.select_cedula(nacionalidad,cedula)
        if not self.paciente:
            self.ventana.mostrar_mensajes("Paciente no encontrado","Paciente no registrado")
            respuesta = self.ventana.preguntar("Registar Paciente","¿Desea Registrar un nuevo paciente?")
            self.paciente = False
            if respuesta == QMessageBox.StandardButton.Yes:
                self.ventana.vista_registrar_pacientes.index=self.ui.stacked_widget.currentIndex()
                self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_pacientes)
                self.ui.line_cedula.setText(cedula)
                self.ui.nacionalidad.setCurrentIndex(self.ui.combo_nacionalidad.currentIndex())
            return 0
    
        self.ui.check_datos_personales.setDisabled(False)
        self.paciente = self.paciente[0]
        self.ui.line_nombre_editar.setText(self.paciente[3])
        self.ui.line_apellido_editar.setText(self.paciente[4])
        año = int(self.paciente[5].strftime("%Y"))
        mes = int(self.paciente[5].strftime("%m"))
        dia = int(self.paciente[5].strftime("%d"))
        self.ui.date_fecha_nacimiento.setDate(QDate(año,mes,dia))
        self.ui.text_direccion_editar.setText(self.paciente[6])
        self.ui.line_telefono_editar.setText(self.paciente[7])
        
        tabla = TablaCitas()
        cita = tabla.select_citas_paciente(str(self.paciente[0]))
        if bool(cita):
            cita = cita[0]
            año = int(cita[1].strftime("%Y"))
            mes = int(cita[1].strftime("%m"))
            dia = int(cita[1].strftime("%d"))
            hora = int(cita[1].strftime("%H"))
            min = int(cita[1].strftime("%M"))
            self.ui.date_proxima_cita.setDateTime(QDateTime(año,mes,dia,hora,min,0))
            self.ui.check_proxima_cita.setDisabled(False)
        else:
            self.ui.check_proxima_cita.setDisabled(True)
        
        tabla = TablaConsultas()
        consulta = tabla.select_consultas_paciente(str(self.paciente[0]))
        if bool(consulta):
            consulta = consulta[0]
            self.ui.text_diagnostico.setText(consulta[2])
            self.ui.text_tratamiento_consulta.setText(consulta[3])
            self.ui.check_consulta.setDisabled(False)
        else:
            self.ui.check_consulta.setDisabled(True)
            
        tabla = TablaAntecedentes()
        antecedentes = tabla.select_antecedente_paciente(str(self.paciente[0]))
        if bool(antecedentes):
            antecedentes = antecedentes[0]
            self.ui.text_patologicos.setText(antecedentes[1])
            self.ui.text_quirurjicos.setText(antecedentes[2])
            self.ui.text_tratamiento.setText(antecedentes[3])
            año = int(antecedentes[4].strftime("%Y"))
            mes = int(antecedentes[4].strftime("%m"))
            dia = int(antecedentes[4].strftime("%d")) 
            self.ui.date_relaciones.setDate(QDate(año,mes,dia))
            self.ui.check_antecedentes.setDisabled(False)
        else:
            self.ui.check_antecedentes.setDisabled(True)
        
        tabla = TablaEmbarazos()
        embarazo = tabla.select_citas_paciente(str(self.paciente[0]))
        if bool(embarazo):
            embarazo = embarazo[0]
            año = int(embarazo[1].strftime("%Y"))
            mes = int(embarazo[1].strftime("%m"))
            dia = int(embarazo[1].strftime("%d"))
            self.ui.date_ultima_regla.setDate(QDate(año,mes,dia))
            año = int(embarazo[2].strftime("%Y"))
            mes = int(embarazo[2].strftime("%m"))
            dia = int(embarazo[2].strftime("%d"))
            self.ui.date_parto.setDate(QDate(año,mes,dia))
            self.ui.check_embarazo.setDisabled(False)
        else:
            self.ui.check_embarazo.setDisabled(True)
            
        self.ui.boton_imprimir.setDisabled(False)
        
    
    def cambiar_datos_personales(self):
        estado =not bool(self.ui.check_datos_personales.isChecked())
        self.ui.line_nombre_editar.setDisabled(estado)
        self.ui.line_apellido_editar.setDisabled(estado)
        self.ui.date_fecha_nacimiento.setDisabled(estado)
        self.ui.line_telefono_editar.setDisabled(estado)
        self.ui.text_direccion_editar.setDisabled(estado)
        self.comprobar_boton_actualizar()
    def cambiar_proxima_cita(self):
        estado =not bool(self.ui.check_proxima_cita.isChecked())
        self.ui.date_proxima_cita.setDisabled(estado)
        self.comprobar_boton_actualizar()
    def cambiar_consulta(self):
        estado =not bool(self.ui.check_consulta.isChecked())
        self.ui.text_diagnostico.setDisabled(estado)
        self.ui.text_tratamiento_consulta.setDisabled(estado)
        self.comprobar_boton_actualizar()
    def cambiar_antecedentes(self):
        estado =not bool(self.ui.check_antecedentes.isChecked())
        self.ui.text_patologicos.setDisabled(estado)
        self.ui.text_quirurjicos.setDisabled(estado)
        self.ui.text_tratamiento.setDisabled(estado)
        self.ui.date_relaciones.setDisabled(estado)
        self.comprobar_boton_actualizar()
    def cambiar_embarazo(self):
        estado =not bool(self.ui.check_embarazo.isChecked())
        self.ui.date_ultima_regla.setDisabled(estado)
        self.ui.date_parto.setDisabled(estado)
        self.comprobar_boton_actualizar()
    
    def comprobar_boton_actualizar(self):
        if self.ui.check_embarazo.isChecked() or self.ui.check_antecedentes.isChecked() or self.ui.check_consulta.isChecked() or self.ui.check_proxima_cita.isChecked() or self.ui.check_datos_personales.isChecked():
            self.ui.boton_actualizar_datos.setEnabled(True)
            self.ui.boton_imprimir.setEnabled(False)
        else:
            self.ui.boton_imprimir.setEnabled(True)
            self.ui.boton_actualizar_datos.setEnabled(False)
    
    def actualizar(self):
        if not bool(self.paciente):
            self.ventana.mostrar_mensajes("Seleccione Paciente","Seleccione un Paciente")
            return 0
        respuesta = self.ventana.preguntar("Confirmar","Se Actualizaran los datos, ¿Confirmar?")
        if respuesta==QMessageBox.StandardButton.No:
            return 0
        
        if self.ui.check_datos_personales.isChecked():
            tabla = TablaPacientes()
            nombre = self.ui.line_nombre_editar.text()
            apellido = self.ui.line_apellido_editar.text()
            fecha = self.ui.date_fecha_nacimiento.date().toString("yyyy-MM-dd")
            telefono = self.ui.line_telefono_editar.text()
            direccion = self.ui.text_direccion_editar.toPlainText()
            if nombre=="" or apellido=="":
                self.ventana.mostrar_mensajes("Datos Invalidos","El nombre y apellido no pueden estar vacios")
                return 0
            if len(telefono)<10:
                self.ventana.mostrar_mensajes("Telefono Invalido","El telefono debe tener al menos 10 digitos")
                return 0
            tabla.update(str(self.paciente[0]),{"nombre":nombre,"apellido":apellido,"fecha_nacimiento":fecha,"dirección":direccion,"telefono":telefono})
            
        if self.ui.check_proxima_cita.isChecked():
            tabla = TablaCitas()
            cita_id = tabla.select_citas_paciente(str(self.paciente[0]))[0][0]
            fecha = self.ui.date_proxima_cita.dateTime().toString("yyyy-MM-dd hh-mm-ss")
            tabla.update(str(cita_id),{"fecha_proxima_cita":fecha})
        if self.ui.check_consulta.isChecked():
            tabla = TablaConsultas()
            consulta_id = tabla.select_consultas_paciente(str(self.paciente[0]))[0][0]
            diagnostico = self.ui.text_diagnostico.toPlainText()
            tratamiento = self.ui.text_tratamiento_consulta.toPlainText()
            if diagnostico=="":
                respuesta = self.ventana.preguntar("Datos Faltantes","El diagnostico esta vacio, ¿Desea Actualizar de todos modos?")
                if respuesta == QMessageBox.StandardButton.No:
                    return 0
            if tratamiento=="":
                respuesta = self.ventana.preguntar("Datos Faltantes","El tratamiento esta vacio, ¿Desea Actualizar de todos modos?")
                if respuesta == QMessageBox.StandardButton.No:
                    return 0
            tabla.update(str(consulta_id),{"diagnostico":diagnostico,"tratamiento":tratamiento})
        if self.ui.check_antecedentes.isChecked():
            tabla = TablaAntecedentes()
            antecedentes_id = tabla.select_antecedente_paciente(str(self.paciente[0]))[0][0]
            patologicos = self.ui.text_patologicos.toPlainText()
            quirurjicos = self.ui.text_quirurjicos.toPlainText()
            tratamiento = self.ui.text_tratamiento.toPlainText()
            if patologicos=="" or quirurjicos=="" or tratamiento=="":
                respuesta = self.ventana.preguntar("Datos Faltantes","Algunos datos de antecedentes estan vacios, ¿Desea Actualizar de todos modos?")
                if respuesta == QMessageBox.StandardButton.No:
                    return 0
            fecha = self.ui.date_relaciones.date().toString("yyyy-MM-dd")
            
            tabla.update(str(antecedentes_id),{"antecedentes_patologicos":patologicos,"antecedentes_quirurjicos":quirurjicos,"tratamiento_actual":tratamiento,"fecha_primera_relacion_sexual":fecha})
            
        if self.ui.check_embarazo.isChecked():
            tabla = TablaEmbarazos()
            embarazo_id = tabla.select_citas_paciente(str(self.paciente[0]))[0][0]
            regla = self.ui.date_ultima_regla.date().toString("yyyy-MM-dd")
            parto = self.ui.date_parto.date().toString("yyyy-MM-dd")
            
            tabla.update(str(embarazo_id),{"fecha_ultima_regla":regla,"fecha_probable_parto":parto})
        
        self.ventana.mostrar_mensajes("Actualizacion Completada","Actualizacion Completada Exitosamente")
        if self.ventana.rol!="USUARIO":
            respuesta = self.ventana.preguntar("Imprimir","¿Imprimir Paciente?")
            if respuesta == QMessageBox.StandardButton.Yes:
                self.imprimir()
        self.reiniciar()
        
    
    def reiniciar(self):
        self.paciente = False
        self.ui.line_nombre_editar.setText("")
        self.ui.line_apellido_editar.setText("")
        self.ui.date_fecha_nacimiento.setDate(QDate(2024,1,1))
        self.ui.line_telefono_editar.setText("")
        self.ui.text_direccion_editar.setText("")
        
        self.ui.date_proxima_cita.setDateTime(QDateTime(2024,1,1,14,0,0))
        
        self.ui.text_diagnostico.setText("")
        self.ui.text_tratamiento_consulta.setText("")
        
        self.ui.text_patologicos.setText("")
        self.ui.text_quirurjicos.setText("")
        self.ui.text_tratamiento.setText("")
        
        self.ui.date_relaciones.setDate(QDate(2024,1,1))
        self.ui.date_ultima_regla.setDate(QDate(2024,1,1))
        self.ui.date_parto.setDate(QDate(2024,1,1))
        
        self.ui.check_proxima_cita.setDisabled(True)
        self.ui.check_consulta.setDisabled(True)
        self.ui.check_antecedentes.setDisabled(True)
        self.ui.check_embarazo.setDisabled(True)
        self.ui.check_datos_personales.setDisabled(True)
        self.ui.boton_imprimir.setDisabled(True)
        
        
        self.ui.check_proxima_cita.setChecked(False)
        self.ui.check_consulta.setChecked(False)
        self.ui.check_antecedentes.setChecked(False)
        self.ui.check_embarazo.setChecked(False)
        self.ui.check_datos_personales.setChecked(False)
        
    def borrar_paciente(self):
        if not self.paciente:
            self.ventana.mostrar_mensajes("No hay Paciente","No hay paciente seleccionado")
            return 0
        
        repuesta = QMessageBox.question(self.ventana,"Eliminar Paciente","Se eliminaran TODOS los datos del paciente incluidos consultas,citas,etc\n¿Estas seguro de eliminar?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        if repuesta == QMessageBox.StandardButton.No:
            return 0
        
        tabla = TablaCitas()
        cita = tabla.select_citas_paciente(str(self.paciente[0]))
        if bool(cita):
            cita = cita[0]
            tabla.delete(str(cita[0]))
            
        tabla = TablaAntecedentes()
        antecedente = tabla.select_antecedente_paciente(str(self.paciente[0]))
        if bool(antecedente):
            antecedente = antecedente[0]
            tabla.delete(str(antecedente[0]))
        
        tabla = TablaEmbarazos()
        embarazo = tabla.select_citas_paciente(str(self.paciente[0]))
        if bool(embarazo):
            embarazo = embarazo[0]
            tabla.delete(str(embarazo[0]))
        
        tabla = TablaConsultas()
        
        consultas = tabla.select_consultas_paciente(str(self.paciente[0]))
        while bool(consultas):
            tabla.delete(str(consultas[0][0]))
            consultas = tabla.select_consultas_paciente(str(self.paciente[0]))

        
        tabla = TablaPacientes()
        tabla.delete(str(self.paciente[0]))
        self.ventana.mostrar_mensajes("Paciente Eliminado","Paciente Eliminado Correctamente")
        
        self.reiniciar()
    
    def imprimir(self):
        nacionalidad = self.ui.combo_nacionalidad.currentText()
        cedula = self.ui.line_cedula_buscar.text()
        nombre = self.ui.line_nombre_editar.text()
        apellido = self.ui.line_apellido_editar.text()
        nacimiento = self.ui.date_fecha_nacimiento.date().toString("yy-MM-dd")
        telefono = self.ui.line_telefono_editar.text()
        direccion = self.ui.text_direccion_editar.toPlainText()
        
        if self.ui.check_proxima_cita.isEnabled():
            proxima_cita = self.ui.date_proxima_cita.dateTime().toString("yy-MM-dd hh-mm")
        else:
            proxima_cita = False
        
        if self.ui.check_consulta.isEnabled():
            diagnostico = self.ui.text_diagnostico.toPlainText()
            tratamiento = self.ui.text_diagnostico.toPlainText()
        else:
            diagnostico = False
            tratamiento = False
        
        if self.ui.check_antecedentes.isEnabled():
            patologicos = self.ui.text_patologicos.toPlainText()
            quirurjicos = self.ui.text_quirurjicos.toPlainText()
            tratamiento_actual = self.ui.text_tratamiento.toPlainText()
            relacion = self.ui.date_proxima_cita.date().toString("yy-MM-dd")

        else:
            patologicos = False
            quirurjicos = False
            tratamiento_actual = False
            relacion = False
        
        if self.ui.check_embarazo.isEnabled():
            regla = self.ui.date_ultima_regla.date().toString("yy-MM-dd")
            embarazo = self.ui.date_parto.date().toString("yy-MM-dd")
        else:
            regla = False
            embarazo = False
        
        pdf = Paciente(nacionalidad,cedula,nombre,apellido,nacimiento,telefono,direccion,proxima_cita,diagnostico,tratamiento,patologicos,quirurjicos,tratamiento_actual,relacion,regla,embarazo)
        
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\SANDIASALUD")
        except FileExistsError:
            pass
        
        path = documentos_path+f"\\SANDIASALUD\\paciente_{nacionalidad}-{cedula}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)

        self.reiniciar()