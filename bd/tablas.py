from bd.conexion import Tabla

class TablaPacientes(Tabla):
    def __init__(self):
        super().__init__("pacientes")
    
    def select_cedula(self,nacionalidad,cedula):
        return self.bd.consultar(f"SELECT * FROM pacientes WHERE cedula={cedula} AND nacionalidad='{nacionalidad}';")

class TablaAntecedentes(Tabla):
    def __init__(self):
        super().__init__("antecedentes")

class TablaEmbarazos(Tabla):
    def __init__(self):
        super().__init__("embarazos")
        
class TablaCitas(Tabla):
    def __init__(self):
        super().__init__("citas")

    def select_citas_paciente(self,id_paciente):
        return self.bd.consultar(f"SELECT * FROM citas WHERE id_paciente={id_paciente};")

    def select_citas_fecha(self,fecha_inicio,fecha_fin):
        return self.bd.consultar(f"CALL buscar_cita('{fecha_inicio}','{fecha_fin}');")
        
class TablaConsultas(Tabla):
    def __init__(self):
        super().__init__("consultas") 

class TablaUsuarios(Tabla):
    def __init__(self):
        super().__init__("usuarios")
    
    def select_usuario(self,usuario):
        return self.bd.consultar(f"SELECT * FROM usuarios WHERE nombre_usuario='{usuario}'")