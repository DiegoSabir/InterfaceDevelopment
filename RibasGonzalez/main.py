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
        var.calendar.Calendar.setSelectedDate((QtCore.QDate(year,mes,dia)))
        var.calendar.Calendar.clicked.connect(drivers.Drivers.cargaFecha)

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

        """
        zona de eventos del tool bar
        """
        #var.ui.actionbarSalir.triggered.connect(eventos.Eventos.cerrarSalir())
        var.ui.actionLimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Main()
        window.show()
        sys.exit(app.exec())