import clientes
from CalendarWindow import *
from dlgAcerca import *
from dlgSalir import *
from datetime import datetime
import var, drivers, eventos


class DlgAcerca(QtWidgets.QDialog):
    def __init__(self):
        super(DlgAcerca, self).__init__()
        var.dlgacerca = Ui_dlgAbout()
        var.dlgacerca.setupUi(self)
        var.dlgacerca.btnCerrar.clicked.connect(eventos.Eventos.cerraracercade)
        var.dlgacerca.lblVersion.setText("Version: " + var.version)



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.calendar.Calendar.clicked.connect(drivers.Drivers.cargaFecha)


        var.calendar.Calendar.clicked.connect(clientes.Clientes.cargaFecha)



class FileDialogAbrir(QtWidgets.QFileDialog):
    def __int__(self):
        super(FileDialogAbrir, self).__int__()
