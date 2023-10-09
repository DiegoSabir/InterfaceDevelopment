import sys, var, eventos

import drivers
from mainwindow import *
from calendar import *
from datetime import datetime

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        year = datetime.now().year

class Main (QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self) #encargado la interfaz
        var.calendar = Calendar()
        var.driver = drivers.Drivers()
        """
        zona de eventos
        """
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        """
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)

        """
        zona de eventos de caja de texto
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDNI)

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Main()
        window.show()
        sys.exit(app.exec())