import clientes
import facturas
import sys, var, eventos, drivers

from CalendarWindow import *
from acercaWindow import *
from salirWindow import *
from datetime import datetime

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        """

        Inicializa la ventana de calendario.

        Establece la fecha actual en el calendario al hacer clic en un botón en otra parte de la aplicación.

        Conecta la señal de clic del calendario a la función cargaFecha en la clase Drivers.

        """
        super(Calendar, self).__init__()
        var.calendar = Ui_calendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        if var.ui.btnCalendario.clicked:
            var.calendar.calendari.setSelectedDate(QtCore.QDate(ano, mes, dia))
            var.calendar.calendari.clicked.connect(drivers.Drivers.cargaFecha)



class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        """

        Inicializa la ventana "Acerca De".

        Conecta el botón de aceptar a la función cerrarAcercaDe en la clase Eventos.

        """
        super(AcercaDe, self).__init__()
        var.acercaDe = Ui_acercaWind()
        var.acercaDe.setupUi(self)

        var.acercaDe.btnaceptar.clicked.connect(eventos.Eventos.cerrarAcercaDe)



class Salir(QtWidgets.QDialog):
    def __init__(self):
        """

        Inicializa la ventana de confirmación de salida.

        Conecta los botones de salir y cancelar a las funciones salir y cerrarSalir en la clase Eventos, respectivamente.

        """
        super(Salir, self).__init__()
        var.salir = Ui_salirwind()
        var.salir.setupUi(self)

        var.salir.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.salir.btnCancelar.clicked.connect(eventos.Eventos.cerrarSalir)



class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        """



        """
        super(FileDialogAbrir, self).__init__()



class Baja(QtWidgets.QDialog):
    def __init__(self):
        """

        Inicializa la ventana de baja para conductores.

        Establece la fecha actual en el calendario al inicializar la ventana.

        Conecta la señal de clic del calendario a la función borraDri en la clase Drivers.

        """
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
        """

        Inicializa la ventana de baja para clientes.

        Establece la fecha actual en el calendario al inicializar la ventana.

        Conecta la señal de clic del calendario a la función borraCli en la clase Clientes.

        """
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
        """

        Inicializa la ventana de alta de facturas.

        Establece la fecha actual en el calendario al inicializar la ventana.

        Conecta la señal de clic del calendario a la función cargaFechafact en la clase Facturas.

        """
        super(Altafact, self).__init__()
        var.Altafact = Ui_calendar()
        var.Altafact.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        anho = datetime.now().year
        var.Altafact.calendari.setSelectedDate(QtCore.QDate(anho, mes, dia))
        var.Altafact.calendari.clicked.connect(facturas.Facturas.cargaFechafact)
