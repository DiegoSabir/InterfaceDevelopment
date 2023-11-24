from datetime import datetime

import conexion
import var
from PyQt6 import  QtWidgets, QtCore, QtGui
class Drivers():
    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.lblCodigo2,var.ui.txtDNI,var.ui.txtApel,var.ui.txtDireccionDriver,var.ui.txtMovil,var.ui.txtSalario,var.ui.txtNombre,var.ui.txtDataDriver,var.ui.lblValidarDni]
            for i in listawidgets:
                i.clear()

            chkLicencia = [var.ui.chkA,var.ui.chkB,var.ui.chkC,var.ui.chkD]
            for i in chkLicencia:
                i.setChecked(False)

            var.ui.cmbProv.setCurrentText(" ")
            var.ui.cmbMuni.setCurrentText(" ")

        except Exception as error:
            print("Error limpiar panel driver",error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtDataDriver.setText(data)
            var.calendar.hide()
        except Exception as error:
            print("Error cargar la fecha",error)

    def validarDNI(self=None):
        try:
            dni = var.ui.txtDNI.text()
            dni = dni.upper()
            var.ui.txtDNI.setText(dni)
            tabla="TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext="XYZ"
            reemp_dig_ext = {'X': '0','Y': '1','Z':'2'}
            numeros = "1234567890"
            if len(dni) == 9 :          #compruebo que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los numero del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0],reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23]==dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDNI.clear()
                    var.ui.txtDNI.setFocus()

            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDNI.clear()
                var.ui.txtDNI.setFocus()
        except Exception as error:
            print("Error al validar dni ",error)

    def altaDriver(self):
        try:
            driver = [var.ui.txtDNI,var.ui.txtDataDriver,
                      var.ui.txtApel,var.ui.txtNombre,var.ui.txtDireccionDriver,
                      var.ui.txtMovil,var.ui.txtSalario]
            newDriver = []
            for i in driver:
                newDriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            newDriver.insert(5, prov)
            muni = var.ui.cmbMuni.currentText()
            newDriver.insert(6, muni)
            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())

            newDriver.append('-'.join(licencias))

           # conexion.Conexion.guardarCli(newDriver)
            '''
            index = 0
            var.ui.tabDrivers.setRowCount(index+1) #Crea una fila
            var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newDriver[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newDriver[1])))
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newDriver[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newDriver[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newDriver[4])))
            var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            '''
            print(newDriver)
            conexion.Conexion.guardarDri(newDriver)

        except Exception as error:
            print("Error alta cliente: ",error)

    def cargarTablaDri(registros):
        try:

            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)  # Crea una fila
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Error alta cliente, error",error)

    def cargaDriver(self):
        try:
            Drivers.limpiarPanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneDriver(fila[0])
            Drivers.cargarDatos(registro)
        except Exception as error:
            print("Error al cargar el cliente marcando la tabla: ",error)

    def buscaDriver(self):
        try:
            dni = var.ui.txtDNI.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.cargarDatos(registro)

            registros = Drivers.selEstado(self=None)
            Drivers.cargarTablaDri(registros)
            codigo = var.ui.lblCodigo2.text()
            Drivers.colorearFila(codigo)

        except Exception as error:
            print("Error al buscar el driver con el dni: ",error)

    def colorearFila(codigo):
        for fila in range(var.ui.tabDrivers.rowCount()):
            if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tabDrivers.columnCount()):
                    item = var.ui.tabDrivers.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarDatos(registro):
        try:
            datos = [var.ui.lblCodigo2, var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel, var.ui.txtNombre,
                     var.ui.txtDireccionDriver, var.ui.cmbProv,
                     var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]
            for j, dato in enumerate(datos):
                if j == 6 or j == 7:
                    dato.setCurrentText(str(registro[j]))
                else:
                    dato.setText(str(registro[j]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
            print(registro)


        except Exception as error:
            print("Error al cargar datos: ",error)

    #Esto marcará el usuario en dicha tabla, hacer que funcione
    def buscarDriverTabla(codigo):
        try:
            tabla = var.ui.tabDrivers
            for fila in range(tabla.rowCount()):
                item = tabla.item(fila, 0)
                valorCelda = item.text()
                if valorCelda == str(codigo):
                    tabla.selectRow(fila)
                    tabla.scrollToItem(item)
        except Exception as error:
            print('No se ha podido seleccionar al driver en la tabla', error)

    def modifDri(self):
        try:
            driver = [var.ui.lblCodigo2,var.ui.txtDNI, var.ui.txtDataDriver,
                      var.ui.txtApel, var.ui.txtNombre, var.ui.txtDireccionDriver,
                      var.ui.txtMovil, var.ui.txtSalario]
            modifDriver = []
            for i in driver:
                modifDriver.append(i.text().title())
            prov = var.ui.cmbProv.currentText()
            modifDriver.insert(6, prov)
            muni = var.ui.cmbMuni.currentText()
            modifDriver.insert(7, muni)
            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())

            modifDriver.append('-'.join(licencias))
            conexion.Conexion.modifDriver(modifDriver)
        except Exception as error:
            print("Error al modificar el usuario: ",error)

    def borraDri(self):
        try:
            dni = var.ui.txtDNI.text()
            conexion.Conexion.borrarDri(dni)

            registros = Drivers.selEstado(self=None)
            Drivers.cargarTablaDri(registros)
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El conductor no existe o no se puede borrar:",error)
            mbox.exec()

    def selEstado(self):
        try:
            if var.ui.rbtTodos.isChecked():
                estado = 0
                registros = conexion.Conexion.consulta_drivers(estado)
                Drivers.cargarTablaDri(registros)

            elif var.ui.rbtAlta.isChecked():
                estado = 1
                registros = conexion.Conexion.consulta_drivers(estado)
                Drivers.cargarTablaDri(registros)

            elif var.ui.rbtBaja.isChecked():
                estado = 2
                registros = conexion.Conexion.consulta_drivers(estado)
                Drivers.cargarTablaDri(registros)

        except Exception as error:
            print("Error al cargar alta los drivers:",error)