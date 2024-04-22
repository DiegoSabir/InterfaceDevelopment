from datetime import datetime

import customers
import events
import var

from CalendarWindow import *
from ExitWindow import *

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_calendar()
        var.calendar.setupUi(self)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        var.calendar.calendari.setSelectedDate((QtCore.QDate(year, month, day)))
        var.calendar.calendari.clicked.connect(customers.Customers.loadDate)



class Exit(QtWidgets.QDialog):
    def __init__(self):
        super(Exit, self).__init__()
        var.exitWindow = Ui_ExitWindow()
        var.exitWindow.setupUi(self)

        '''
            Zona de Eventos de botones de dlgSalir
        '''

        var.exitWindow.btnOk.clicked.connect(events.Events.confirmExit)
        var.exitWindow.btnCancel.clicked.connect(events.Events.cancelExit)
