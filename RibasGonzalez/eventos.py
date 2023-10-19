import var, sys
from PyQt6 import QtWidgets,QtCore
from datetime import datetime

class Eventos():
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print(error, "en modulo eventos")

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error al abrir calendar", error)

    @staticmethod
    def acercade():
        try:
            pass
        except Exception as error:
            print("error al abrir acercade", error)

    @staticmethod
    def cerraracercade():
        try:
            var.dlgacerca.hide()
        except Exception as error:
            print("error abrir ventana acercade", error)

    def cargastatusbar(self):
        """
        Formatear la fecha según el formato deseadofecha_actual.strftime()
        statusbar
        """
        try:
            fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)

        except Exception as error:
            print('Error cargar el statusbar: ', error)

    def cargaprov(self = None):
        try:
            prov = ["A Coruña", "Lugo", "Vigo", "Ferrol", "Santiago de Compostela", "Ourense", "Pontevedra"]
            var.ui.cmbProv.clear()
            var.ui.cmbProv.addItem("")
            for i,m in enumerate(prov):
                var.ui.cmbProv.addItem(str(m))

        except Exception as error:
            print("error en la carga del combo prov", error)

    def selEstado(self):
        if var.ui.crbtTodos.isChecked():
            print("pulsaste todos")
        elif var.ui.rbtAlta.isChecked():
            print("pulsaste alta")
        elif var.ui.rbtBaja.isChecked():
            print("pulsaste baja")