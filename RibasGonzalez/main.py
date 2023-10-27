from drivers import *
from MainWindow import *
from windowaux import *
from dlgSalir import *
import var, drivers, sys, eventos
import conexion

# Establecer la configuración regional en español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.dlgacerca = DlgAcerca()
        var.dlgsalir = DlgSalir()
        self.driver = Drivers()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()

        '''
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)

        """
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        '''
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(Drivers.validarDNI)
        var.ui.txtMovil.editingFinished.connect(Drivers.validarMovil)
        var.ui.txtNome.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajatexto)

        '''
         eventos del toolbar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionlimpiaPaneldriver.triggered.connect(drivers.Drivers.limpiapanel)

        '''
        eventos de tablas        
        '''
        eventos.Eventos.resizeTabdrivers(self)

        '''
        ejecución de diferentes funciones al lanzar la aplicación
        '''
        eventos.Eventos.cargastatusbar(self)
        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)


    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.mostrarsalir()
        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
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
