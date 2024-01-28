import clientes
import conexion
import facturas
import informes
from mainWindows import *
from PyQt6.QtCore import QTimer,QSize
from auxiliar import *
import locale


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

import sys, var, eventos, drivers
class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar=Calendar()
        var.salir=Salir()
        var.Baja = Baja()
        var.Bajacli = Bajacli()
        var.Altafact = Altafact()
        var.acercaDe=AcercaDe()
        self.cargarStatusbar()
        conexion.Conexion.conexion()
        conexion.Conexion.cargarprov()
        conexion.Conexion.mostrardriver()
        conexion.Conexion.cargarprov2()
        conexion.Conexion.cargarprov3()
        conexion.Conexion.cargarprov4()
        conexion.Conexion.cargarconductor()
        conexion.Conexion.mostrarClientes()
        conexion.Conexion.cargarfacturas()
        var.dlgabrir = FileDialogAbrir()

        '''
        Eventos 
        '''
        rbtClientes = (var.ui.rbtTodos2, var.ui.rbtAlta2, var.ui.rbtBaja2)
        for i in rbtClientes:
            i.toggled.connect(eventos.Eventos.selEstado2)
        rbtDriver=(var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja)
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)
        '''
        Eventos Botones
        '''
        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver)
        var.ui.btnBuscar.clicked.connect(drivers.Drivers.buscaDri)
        var.ui.btnModificarDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(eventos.Eventos.abrirCalendarBaja)
        var.ui.btnAlta2.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnModificar2.clicked.connect(clientes.Clientes.modifCli)
        var.ui.btnBaja2.clicked.connect(eventos.Eventos.abrirCalendarBajacli)
        var.ui.btnBuscar2.clicked.connect(clientes.Clientes.buscarCliente)
        var.ui.btnBuscar3.clicked.connect(facturas.Facturas.buscarClifact)
        var.ui.btnCalendariofact.clicked.connect(eventos.Eventos.abrirCalendarfact)
        var.ui.btnFactura.clicked.connect(facturas.Facturas.altafactura)
        var.ui.btngrabar.clicked.connect(facturas.Facturas.guardarViaje)


        '''
        zona eventos menu bar
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionAcercaDe.triggered.connect(eventos.Eventos.abrirAcercaDe)
        var.ui.actionCrear_copia_de_seguridad.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_copia_de_seguridad.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionExportar_datos_xls.triggered.connect(eventos.Eventos.exportardatosxls)
        var.ui.actionImportar_datos_xls.triggered.connect(eventos.Eventos.importarDatosExcel)
        var.ui.actionExportar_datos_clientes_xls.triggered.connect(eventos.Eventos.exportardatosclientesxls)
        var.ui.actionImportar_datos_clientes_xls.triggered.connect(eventos.Eventos.importarDatosclientesExcel)
        var.ui.actionCrear_informe_pdf.triggered.connect(informes.Informes.reportclientes)
        var.ui.actionCrear_informe_conductores.triggered.connect(informes.Informes.reportdrivers)
        var.ui.actionCrear_informe.triggered.connect(informes.Informes.checkboxinforme)
        '''
        combobox
        '''
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.cmbProv2.currentIndexChanged.connect(conexion.Conexion.selMuni2)
        var.ui.cmbProbVentas.currentIndexChanged.connect(conexion.Conexion.selMuni3)
        var.ui.cmbProbVentas.currentIndexChanged.connect(conexion.Conexion.datosViaje)
        var.ui.cmbMuniVentas.currentIndexChanged.connect(conexion.Conexion.datosViaje)
        var.ui.cmbProbVentas2.currentIndexChanged.connect(conexion.Conexion.selMuni4)
        var.ui.cmbProbVentas2.currentIndexChanged.connect(conexion.Conexion.datosViaje)
        var.ui.cmbMuniVentas2.currentIndexChanged.connect(conexion.Conexion.datosViaje)

        '''
        Eventos cajas texto
        '''
        var.ui.txtDNI.editingFinished.connect(eventos.Eventos.validarDNI)
        var.ui.txtsalario.editingFinished.connect(drivers.Drivers.validarSalario)
        var.ui.txtmovil.editingFinished.connect(drivers.Drivers.validarMovil)
        var.ui.txtnombre.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtapellidos.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtsalario.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtDNI2.editingFinished.connect(eventos.Eventos.validarDNI2)
        var.ui.txtmovil2.editingFinished.connect(clientes.Clientes.validarMovil2)
        var.ui.txtkm.editingFinished.connect(facturas.Facturas.validarKm)
        '''
        Eventos tabla 
         '''
        var.ui.actionvarsalir.triggered.connect(eventos.Eventos.abrirSalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)
        var.ui.actionlimpiarPanel.triggered.connect(clientes.Clientes.limpiarPanel2)
        var.ui.actionlimpiarPanel.triggered.connect(facturas.Facturas.limpiarPanel3)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargarDriver)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargarCliente)
        var.ui.tablaFacturas.clicked.connect(facturas.Facturas.cargarFactura)
        var.ui.tabViajes.clicked.connect(facturas.Facturas.cargarViaje)
        '''
        Eventos 
        '''
        eventos.Eventos.resizeTabdrivers(self)
        eventos.Eventos.resizeTabclientes(self)
        eventos.Eventos.resizeTabfacturas()
        eventos.Eventos.resizeTabViajes()

    def closeEvent(self, event):
        event.ignore()
        eventos.Eventos.abrirSalir(self)

    def cargarStatusbar(self):
        self.labelVersion = QtWidgets.QLabel("Version: 0.1.0", self)
        self.labelVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.labelVersion.setStyleSheet("margin-left: 10px;")
        var.ui.statusbar.addPermanentWidget(self.labelVersion, 0)
        self.actualizarFecha()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizarFecha)
        self.timer.start(60000)

    def actualizarFecha(self):
        if hasattr(self, 'labelstatus') and self.labelstatus is not None:
            var.ui.statusbar.removeWidget(self.labelstatus)
            self.labelstatus = None
        self.labelstatus = QtWidgets.QLabel(datetime.now().strftime('%A - %d/%m/%Y'), self)
        self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        var.ui.statusbar.addPermanentWidget(self.labelstatus, 2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
