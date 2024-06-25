from fpdf import FPDF
import os

class Consulta(FPDF):
    invoice_counter = 0  

    def __init__(self, consulta, nacionalidad, cedula, nombre, apellido, diagnostico, tratamiento, fecha,proxima_cita,regla,embarazo):
        super().__init__()
        Consulta.invoice_counter += 1
        self.consuta = consulta
        self.nacionalidad = nacionalidad
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.fecha = fecha
        self.proxima_cita = proxima_cita
        self.regla = regla
        self.embarazo = embarazo
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_invoice_info()
        self.add_client_info()
        self.add_body()
        self.add_footer()

    def add_logo(self):
        logo_path = 'images/logo_sin_fondo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'CONSULTA', 0, 1, 'C')
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'SANDIA SALUD', 0, 1, 'C')
        self.cell(0, 10, 'DOCTORA SAILE SANDIA', 0, 1, 'C')
        self.set_font('Arial', 'B', 12)
        self.cell(0,10,'Barrio obrero, calle 10 con carrera 17',0,1,'C')
        self.cell(0,10,' subiendo por el cuartel bolivar, San Cristóbal estado Táchira',0,1,'C')

    def add_invoice_info(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Contacto: 0414-4146541', 0, 1, 'C')
        self.cell(0, 10, f'NUMERO DE CONSULTA: {self.consuta}', 0, 1, 'C')
        self.cell(0, 5, f'Fecha: {self.fecha}', 0, 1, 'C')
        if self.proxima_cita:
            self.cell(0, 5, f'Proxima Cita: {self.proxima_cita}', 0, 1, 'C')
            

    def add_client_info(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 5, 'PACIENTE:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 5, f'CEDULA: {self.nacionalidad}-{self.cedula}', 0, 1, 'L')
        self.cell(0, 5, f'NOMBRE: {self.nombre}', 0, 1, 'L')
        self.cell(0, 5, f'APELLIDO: {self.apellido}', 0, 1, 'L')

    def add_body(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 8, '', 0, 1, 'L')
        self.cell(0, 10, f'Diagnostico:', 0, 1, 'L')
        self.set_font('Arial', '', 14)
        self.multi_cell(0, 5, f'{self.diagnostico}', 0, 1, 'L')
        self.cell(0, 10, '', 0, 1, 'L')
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f'Tratamiento:', 0, 1, 'L')
        self.set_font('Arial', '', 14)
        self.multi_cell(0, 5, f'{self.tratamiento}', 0, 1, 'L')
        if self.regla and self.embarazo:
            self.cell(0, 14, '', 0, 1, 'L')
            self.cell(0, 5, f'Ultima Regla: {self.regla}', 0, 1, 'L')
            self.cell(0, 5, f'Fecha Probable de Parto: {self.embarazo}', 0, 1, 'L')

    def add_footer(self):
        self.set_y(250)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'______________________________', 0, 1, 'C')
        self.cell(0, 10, f'FIRMA', 0, 1, 'C')
        
