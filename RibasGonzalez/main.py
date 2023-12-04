from MainWindow import *
from windowaux import *

import var
import drivers
import sys
import eventos
import locale
import conexion


# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):


    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.dlgacerca = DlgAcerca()
        var.dlgAbrir = FileDialogAbrir()
        #self.driver = Drivers()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()
        estado = 1
        conexion.Conexion.selectDrivers(estado)



        '''
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)
        var.ui.btnBuscadri.clicked.connect(drivers.Drivers.buscaDri)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrarDriv)


        """
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(eventos.Eventos.restaurarbackup)
        var.ui.actionExportar_Datos_Excel.triggered.connect(eventos.Eventos.exportardatosxls)
        var.ui.actionImportar_Datos_XLS.triggered.connect(eventos.Eventos.importardatosxls)


        '''
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDNI(var.ui.txtDni.text()))
        #var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDNI(var.ui.txtDni.displayText()))

        var.ui.txtNome.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtMovil.editingFinished.connect(eventos.Eventos.formatCajamovil)


        '''
        eventos del toolbar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionlimpiaPaneldriver.triggered.connect(drivers.Drivers.limpiapanel)
        var.ui.actioncrearbackup.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionrestaurarbackup.triggered.connect(eventos.Eventos.restaurarbackup)


        '''
        eventos de tablas        
        '''
        eventos.Eventos.resizeTabdrivers(self)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargadriver)


        '''
        eventos combobox
        '''
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.rtbGroup.buttonClicked.connect(drivers.Drivers.selEstado)




    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.mostrarsalir()
        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
                                                 QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        if mbox == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()



if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication([])
        window = Main()
        window.showMaximized()
        sys.exit(app.exec())

    except Exception as error:
        print(error)