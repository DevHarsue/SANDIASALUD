from PySide6.QtCore import QDate,Qt
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem
from datetime import datetime,time
from bd.tablas import TablaCitas


class VistaCitas:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.preparar()
        
    def preparar(self):
        self.ui.date_cita_desde.setDate(QDate(2024,1,1))
        self.ui.date_cita_hasta.setDate(QDate(2024,1,31))
        self.ui.check_rango_cita.stateChanged.connect(self.cambiar_busqueda)
        self.ui.boton_buscar_cita.pressed.connect(self.buscar_citas)
        self.ui.check_rango_cita.setChecked(False)
        self.ui.date_cita_hasta.setDisabled(True)
    
    def buscar_citas(self):
        while self.ui.tabla_citas.rowCount() > 0:
            self.ui.tabla_citas.removeRow(0)
            
        fecha_inicio = self.ui.date_cita_desde.dateTime().toString("yyyy-MM-dd") +" 00-00-00"
        fecha_fin = self.ui.date_cita_hasta.dateTime().toString("yyyy-MM-dd") +" 23-59-59"
        tabla = TablaCitas()
        if self.ui.check_rango_cita.isChecked():
            citas = tabla.select_citas_fecha(fecha_inicio,fecha_fin)
        else:
            citas = tabla.select_citas_fecha(fecha_inicio,fecha_inicio[0:10]+" 23-59-59")
            
        for i,x in enumerate(citas):
            self.ui.tabla_citas.insertRow(self.ui.tabla_citas.rowCount())
            self.ui.tabla_citas.setItem(i,0,QTableWidgetItem(str(x[1])))
            self.ui.tabla_citas.setItem(i,1,QTableWidgetItem(str(x[2])))
            self.ui.tabla_citas.setItem(i,2,QTableWidgetItem(str(x[3])))
            self.ui.tabla_citas.setItem(i,3,QTableWidgetItem(str(x[4])))
            self.ui.tabla_citas.setItem(i,4,QTableWidgetItem(str(x[5].strftime("%d/%m/%Y  %H:%M:%S"))))
    
    def cambiar_busqueda(self,estado):
        if estado == 0:
            self.ui.date_cita_hasta.setDisabled(True)
        elif estado == 2:
            self.ui.date_cita_hasta.setDisabled(False)
            