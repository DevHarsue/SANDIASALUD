from PySide6.QtWidgets import QMainWindow, QApplication
from interfaz.interfaz_principal import Ui_MainWindow
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    sys.exit(app.exec())