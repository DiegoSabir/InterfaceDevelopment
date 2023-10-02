import eventos
from mainwindow import *
import sys, var

class Main (QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_WindowMain()
        var.ui.setupUi(self) #encargado la interfaz

        """
        zona de eventos
        """
        var.ui.btnSalir.clicked.connect(eventos.Eventos.saludar)

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Main()
        window.show()
        sys.exit(app.exec())