from datetime import datetime

import customers
import events
import invoices
import var

from CalendarWindow import *
from ExitWindow import *
from ModifyFireWindow import *


class Fire(QtWidgets.QDialog):
    def __init__(self):
        super(Fire, self).__init__()
        var.dlgModifyFireWindow = Ui_dlgModifyFireWindow()
        var.dlgModifyFireWindow.setupUi(self)

        var.dlgModifyFireWindow.btnModifyFireDateYes.clicked.connect(events.Events.confirmModify)
        var.dlgModifyFireWindow.btnModifyFireDateNo.clicked.connect(events.Events.cancelModify)


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


class CalendarInvoice(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarInvoice, self).__init__()
        var.calendarInvoice = Ui_calendar()
        var.calendarInvoice.setupUi(self)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        var.calendarInvoice.calendari.setSelectedDate((QtCore.QDate(year, month, day)))
        var.calendarInvoice.calendari.clicked.connect(invoices.Invoices.load_date)


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


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
