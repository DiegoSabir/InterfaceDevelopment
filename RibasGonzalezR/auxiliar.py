import sys
import var
import customer

from CalendarWindow import *
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
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        if var.ui.btnCalendario.clicked:
            var.calendar.calendari.setSelectedDate(QtCore.QDate(year, month, day))
            var.calendar.calendari.clicked.connect(customer.Customer.loadDate)