import var, eventos
from PyQt6 import QtWidgets
class Drivers():

    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtFecha, var.ui.txtApel, var.ui.txtNom,
                            var.ui.txtDir, var.ui.txtMovil, var.ui.txtSalario, var.ui.lblValidarDni]
            for i in listawidgets:
                i.setText(None)

            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                i.setChecked(False)

            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')

        except Exception as error:
            print("error en limpiar panel driver: ", error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha:", error)

    def validarDNI(self = None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            if len(dni) == 9:  # compruebo que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)

    def altadriver(self):
        try:
            driver = [var.ui.txtApel, var.ui.txtNom, var.ui.txtMovil]
            newdriver = []
            newdriver.append(1)
            for i in driver:
                newdriver.append(i.text().title())1
            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdriver.append('-'.join(licencias))
            index = 0
            var.ui.tabDrivers.setRowCount(index+1) #crea una fila
            var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newdriver[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdriver[1])))
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdriver[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdriver[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdriver[4])))

            print(newdriver)

        except Exception as error:
            print("error alta cliente", error)