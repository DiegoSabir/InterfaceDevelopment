from drivers import *
from mainwindow import *
from windowaux import *
from salir import *
import var, drivers, sys, eventos
from datetime import datetime


#Establecer la configuracion regional en español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

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
        var.ui.actionSalir.triggered.connect(eventos.Eventos.acercade)

        """
        zona de eventos de caja de texto
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDNI)

        """
        zona de eventos del tool bar
        """
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.cerrarSalir())
        var.ui.actionLimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)

        """
        eventos de tablas
        """



        """
        ejecucion de diferentes funciones al lanzar la aplicacion
        """
        eventos.Eventos.cargastatusbar(self)
        eventos.Eventos.cargaprov(self)
        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)

    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estas seguro de que quieres salir?',
                                                     QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        if mbox == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Main()
        window.show()
        sys.exit(app.exec())