import var, eventos
from PyQt6 import QtWidgets, QtCore


class Drivers():
    def limpiapanel(self):
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                            var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario, var.ui.lblValidardni ]

            for i in listawidgets:
                i.setText(None)

            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
               i.setChecked(False)
            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')
        except Exception as error:
            print('error limpia panel driver: ', error)


    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDatadriver.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha: ", error)


    @staticmethod
    def validarDNI(self = None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper() #poner mayúscula
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9 :          #comprueba que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:
                    var.ui.lblValidardni.setStyleSheet('color:green;') # si es válido se pone una V en color verde
                    var.ui.lblValidardni.setText('V')
                else:
                    var.ui.lblValidardni.setStyleSheet('color:red;') #y si no un aspa en color rojo
                    var.ui.lblValidardni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidardni.setStyleSheet('color:red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)


    def altadriver(self):
        try:
            driver = [var.ui.txtApel, var.ui.txtNome, var.ui.txtMovil]
            newdriver = []
            newdriver.append(1)
            for i in driver:
                newdriver.append(i.text().title())
            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdriver.append('-'.join(licencias))
            index = 0
            var.ui.tabDrivers.setRowCount(index+1) #crea una fila
            var.ui.tabDrivers.setItem(index,0,QtWidgets.QTableWidgetItem(str(newdriver[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdriver[1])))
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdriver[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdriver[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdriver[4])))
            var.ui.tabDrivers.item(index,0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        except Exception as error:
            print("error alta cliente", error)