import eventos, var, drivers
from calendar import *
from salir import *
from acercade import *
from datetime import datetime


class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe,self).__init__()
        var.acercaDe = Ui_dlgAcercaDe()
        var.acercaDe.setupUi(self)

        """ 
         Zona de eventos de botones
        """
        var.acercaDe.BtnAceptar.clicked.connect(eventos.Eventos.cerrarAcercaDe)


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir,self).__init__()
        var.salir = Ui_dlgSalir()
        var.salir.setupUi(self)

        """ 
         Zona de eventos de botones
        """

        var.salir.BtnAccept.clicked.connect(eventos.Eventos.salir)
        var.salir.BtnCancel.clicked.connect(eventos.Eventos.cerrarAcercaDe)


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        year = datetime.now().year
        var.calendar.calendar.setSelectedDate((QtCore.QDate(year,mes,dia)))
        var.calendar.calendar.clicked.connect(drivers.Drivers.cargaFecha)