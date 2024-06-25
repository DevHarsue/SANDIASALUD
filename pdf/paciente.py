from fpdf import FPDF
import os

class Paciente(FPDF):
    invoice_counter = 0  

    def __init__(self, nacionalidad, cedula, nombre, apellido, nacimiento, telefono, direccion, proxima_cita, diagnostico, tratamiento, patologicos, quirurjicos, tratamiento_actual,relacion,regla,embarazo):
        super().__init__()
        Paciente.invoice_counter += 1
        self.nacionalidad = nacionalidad
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.telefono = telefono
        self.direccion = direccion
        self.proxima_cita = proxima_cita
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.patologicos = patologicos
        self.quirurjicos = quirurjicos
        self.tratamiento_actual = tratamiento_actual
        self.relacion = relacion
        self.regla = regla
        self.embarazo = embarazo
        
        self.total = 0
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_invoice_info()
        self.add_client_info()
        self.add_table()

    def add_logo(self):
        logo_path = 'images/logo_sin_fondo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'INFORMACION PACIENTE', 0, 1, 'C')
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'SANDIA SALUD', 0, 1, 'C')
        self.cell(0, 10, 'DOCTORA SAILE SANDIA', 0, 1, 'C')
        self.set_font('Arial', 'B', 12)
        self.cell(0,10,'Barrio obrero, calle 10 con carrera 17',0,1,'C')
        self.cell(0,10,' subiendo por el cuartel bolivar, San Cristóbal estado Táchira',0,1,'C')


    def add_invoice_info(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Contacto: 0414-4146541', 0, 1, 'C')
        if self.proxima_cita:
            self.cell(0, 5, f'Proxima Cita: {self.proxima_cita}', 0, 1, 'C')

    def add_client_info(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 5, 'PACIENTE:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 5, f'CEDULA: {self.nacionalidad}-{self.cedula}', 0, 1, 'L')
        self.cell(0, 5, f'NOMBRE: {self.nombre}', 0, 1, 'L')
        self.cell(0, 5, f'APELLIDO: {self.apellido}', 0, 1, 'L')
        self.cell(0, 5, f'FECHA DE NACIMIENTO: {self.nacimiento}', 0, 1, 'L')
        self.cell(0, 5, f'TELEFONO: {self.telefono}', 0, 1, 'L')
        self.multi_cell(0, 5, f'DIRECCION: {self.direccion}', 0, 1, 'L')

    def add_table(self):
        if self.diagnostico:
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, f'', 0, 1, 'L')
            self.cell(0, 10, f'Diagnostico:', 0, 1, 'L')
            self.set_font('Arial', '', 14)
            self.multi_cell(0, 5, f'{self.diagnostico}', 0, 1, 'L')
        if self.tratamiento:
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, f'Tratamiento:', 0, 1, 'L')
            self.set_font('Arial', '', 14)
            self.multi_cell(0, 5, f'{self.tratamiento}', 0, 1, 'L')
        
        if self.patologicos:
            self.set_font('Arial', 'B', 14)        
            self.cell(0, 10, f'Antecedentes Patologicos:', 0, 1, 'L')
            self.set_font('Arial', '', 14)
            self.multi_cell(0, 5, f'{self.patologicos}', 0, 1, 'L')
        
        if self.quirurjicos:
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, f'Antecedentes Quirurjicos:', 0, 1, 'L')
            self.set_font('Arial', '', 14)
            self.multi_cell(0, 5, f'{self.quirurjicos}', 0, 1, 'L')
        
        if self.tratamiento_actual:
            self.set_font('Arial', 'B', 14)
            self.cell(0, 10, f'Antecedentes de Tratamiento:', 0, 1, 'L')
            self.set_font('Arial', '', 14)
            self.multi_cell(0, 5, f'{self.tratamiento_actual}', 0, 1, 'L')
        
        self.cell(0, 5, f'', 0, 1, 'L')
        if self.relacion:
            self.cell(0, 5, f'Fecha de primera relacion sexual: {self.relacion}', 0, 1, 'L')
        if self.regla:
            self.cell(0, 5, f'Fecha de ultima regla: {self.regla}', 0, 1, 'L')
        if self.embarazo:
            self.cell(0, 5, f'Fecha probable de parto: {self.embarazo}', 0, 1, 'L')
        
