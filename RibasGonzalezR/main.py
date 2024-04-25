import locale
import sys

import customers
import events
import var
import connection
import auxiliary

from MainWindow import *
from auxiliary import *

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.exitWindow = Exit()
        connection.Connection.connection()


        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(events.Events.openCalendar)
        var.ui.btnEnroll.clicked.connect(customers.Customers.enrollCustomer)
        var.ui.btnModify.clicked.connect(customers.Customers.modifyCustomer)


        '''
        Zona de eventos da toolbar
        '''
        var.ui.actionSalir.triggered.connect(events.Events.showExit)
        var.ui.actionlimpiarPanel.triggered.connect(customers.Customers.clear)


        '''
        Zona de init
        '''
        connection.Connection.showCustomers()




    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox()
        mbox.setStyleSheet("QDialog{background-color: #8294C4;} "
                           "QLabel {color: rgb(0, 0, 0);} ")
        mbox.setWindowTitle("Exit")
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setText("¿Do you want to Exit?")

        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Yes')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        resultado = mbox.exec()

        if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())