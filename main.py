from PySide6.QtWidgets import QMainWindow, QApplication,QDateEdit
from interfaz.interfaz_principal import Ui_MainWindow
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.asignar_slots_vistas()
        self.show()
    
    def asignar_slots_vistas(self):
        self.ui.boton_v_agendar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentIndex(4))
        self.ui.boton_v_citas.pressed.connect(lambda:self.ui.stacked_widget.setCurrentIndex(0))
        self.ui.boton_v_consulta.pressed.connect(lambda:self.ui.stacked_widget.setCurrentIndex(5))
        self.ui.boton_v_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentIndex(2))
        self.ui.boton_v_registrar_pacientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentIndex(1))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    sys.exit(app.exec())