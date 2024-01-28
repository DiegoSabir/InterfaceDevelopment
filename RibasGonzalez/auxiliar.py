import clientes
import facturas
from calendarWindow import *
from acercaWindow import *
from salirWindow import *
from datetime import datetime

import sys, var, eventos, drivers
class Calendar(QtWidgets.QDialog):
    def __init__(self):
        bool=None
        super(Calendar, self).__init__()
        var.calendar = Ui_calendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        if var.ui.btnCalendario.clicked:
            var.calendar.calendari.setSelectedDate(QtCore.QDate(ano,mes,dia))
            var.calendar.calendari.clicked.connect(drivers.Drivers.cargaFecha)
class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        var.acercaDe = Ui_acercaWind()
        var.acercaDe.setupUi(self)

        var.acercaDe.btnaceptar.clicked.connect(eventos.Eventos.cerrarAcercaDe)


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self).__init__()
        var.salir = Ui_salirwind()
        var.salir.setupUi(self)

        var.salir.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.salir.btnCancelar.clicked.connect(eventos.Eventos.cerrarSalir)
class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
class Baja(QtWidgets.QDialog):
    def __init__(self):
        super(Baja, self).__init__()
        var.Baja = Ui_calendar()
        var.Baja.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.Baja.calendari.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.Baja.calendari.clicked.connect(drivers.Drivers.borraDri)

class Bajacli(QtWidgets.QDialog):
    def __init__(self):
        super(Bajacli, self).__init__()
        var.Bajacli = Ui_calendar()
        var.Bajacli.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.Bajacli.calendari.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.Bajacli.calendari.clicked.connect(clientes.Clientes.borraCli)

class Altafact(QtWidgets.QDialog):
    def __init__(self):
        super(Altafact, self).__init__()
        var.Altafact = Ui_calendar()
        var.Altafact.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.Altafact.calendari.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.Altafact.calendari.clicked.connect(facturas.Facturas.cargaFechafact)
