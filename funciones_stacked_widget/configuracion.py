from PySide6.QtWidgets import QMessageBox
from ventanas import VentanaConfiguracion,VentanaUsuarios


class VistaConfiguracion:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_crear_usuarios.pressed.connect(self.cambiar_crear_usuarios)
        self.ui.boton_configurar_bd.pressed.connect(self.configurar_bd)
    
    def cambiar_crear_usuarios(self):
        self.ventana.close()
        self.ventana_nueva = VentanaUsuarios(self.ventana)
        self.ventana_nueva.ui.combo_tipo.removeItem(0)
        self.ventana_nueva.show()
        self.ventana_nueva.ui.boton_volver.setDisabled(False)
        
    def configurar_bd(self):
        
        self.ventana.close()
        self.ventana_nueva = VentanaConfiguracion(self.ventana)
        self.ventana_nueva.show()
        self.ventana_nueva.ui.boton_volver.setDisabled(False)
        