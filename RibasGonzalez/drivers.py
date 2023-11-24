from datetime import datetime

import locale
import var, eventos, conexion
from PyQt6 import QtWidgets, QtCore, QtGui

class Drivers():
    def limpiapanel(self):
        try:
            listawidgets = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtNome, var.ui.txtApel, var.ui.txtDirdriver, var.ui.txtSalario,
                            var.ui.txtMovil, var.ui.lblValidardni]
            for i in listawidgets:
                i.clear()

            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                i.setChecked(False)

            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')

            if var.ui.rbtAlta.isChecked():
                estado = 1
                conexion.Conexion.selectDrivers(estado)
            else:
                registros = conexion.Conexion.mostrardrivers(self)
                Drivers.cargartabladri(registros)

        except Exception as error:
            print('error limpia panel driver: ', error)


    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDatadriver.setText(data)
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
            if len(dni) == 9:          #comprueba que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:
                    var.ui.lblValidardni.setStyleSheet('color:green;')# si es válido se pone una V en color verde
                    var.ui.lblValidardni.setText('V')
                else:
                    var.ui.lblValidardni.setStyleSheet('color:red;')
                    var.ui.lblValidardni.setText('X')
                    var.ui.txtDni.clear()
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidardni.setStyleSheet('color:red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.clear()
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)

    @staticmethod
    def validarMovil(self = None):
        try:
            movil = var.ui.txtMovil.text()
            numeros = "1234567890"
            for n in movil:
                if n in numeros and len(movil) == 9:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso: numero movil incorrecto')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Escriba un número de móvil correcto')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtMovil.setText("")
                    break
        except Exception as error:
            print("error en validar movil ", error)

    def altadriver(self):
        try:
            driver = [var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                      var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario]
            newdriver = []

            for i in driver:
                if i.text().strip():
                    newdriver.append(i.text().title())
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Tods los campos deben ser rellenados: \n DNI, Nombre, Fecha de alta y Movil")
                    mbox.exec()

            prov = var.ui.cmbProv.currentText()
            newdriver.insert(5,prov)
            muni = var.ui.cmbMuni.currentText()
            newdriver.insert(6,muni)
            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdriver.append('-'.join(licencias))

            print(newdriver)
            conexion.Conexion.guardardri(newdriver)

        except Exception as error:
            print("error alta cliente", error)

    def formatCajatexto(self = None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            salario = var.ui.txtSalario.text()
            valores = "1234567890."
            for n in salario:
                if n in valores:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('Valor de Salario Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtSalario.setText("")
                    break
            var.ui.txtSalario.setText(str(locale.currency(round(float(var.ui.txtSalario.text()),2), grouping=True)))
        except Exception as error:
            print('error poner letra capital cajas text', error)


    def cargartabladri(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index+1) #crea una fila
                var.ui.tabDrivers.setItem(index,0,QtWidgets.QTableWidgetItem(str(registro[0])))
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
            print("error alta cliente", error)

    def cargadriver(self):
        try:
            Drivers.limpiapanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onedriver(fila[0])
            Drivers.cargadatos(registro)

        except Exception as error:
            print("error al cargar el cliente marcando la tabla: ", error)

    def buscaDri(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.cargadatos(registro)

            registros = Drivers.selEstado(self=None)
            Drivers.cargartabladri(registros)
            codigo = var.ui.lblcodbd.text()
            Drivers.colorearFila(codigo)

        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def colorearFila(codigo):
        for fila in range(var.ui.tabDrivers.rowCount()):
            if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tabDrivers.columnCount()):
                    item = var.ui.tabDrivers.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))


    def cargadatos(registro):
        try:
            datos = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                     var.ui.txtDirdriver, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            else:
                var.ui.chkA.setChecked(False)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            else:
                var.ui.chkB.setChecked(False)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            else:
                var.ui.chkC.setChecked(False)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
            else:
                var.ui.chkD.setChecked(False)
        except Exception as error:
            print("cargar datos en panel gestión", error)

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
            driver = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver,
                      var.ui.txtApel, var.ui.txtNome, var.ui.txtDirdriver,
                      var.ui.txtMovil, var.ui.txtSalario]
            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            modifdriver.insert(6, prov)
            muni = var.ui.cmbMuni.currentText()
            modifdriver.insert(7, muni)
            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())

            modifdriver.append('-'.join(licencias))
            conexion.Conexion.modifDriver(modifdriver)

        except Exception as error:
            print("error en modif drivaer en Drivers", error)

    def borrarDri(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borrarDri(dni)

            #conexion.Conexion.mostrardrivers(self)
            registros = Drivers.selEstado(self=None)
            Drivers.cargartabladri(registros)

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El conductor no existe o no se puede borrar")
            mbox.exec()

    def selEstado(self):
        try:
            if var.ui.rbtTodos.isChecked():
                estado = 0
                registros = conexion.Conexion.selectDrivers(estado)
                Drivers.cargartabladri(registros)

            elif var.ui.rbtAlta.isChecked():
                estado = 1
                registros = conexion.Conexion.selectDrivers(estado)
                Drivers.cargartabladri(registros)

            elif var.ui.rbtBaja.isChecked():
                estado = 2
                registros = conexion.Conexion.selectDrivers(estado)
                Drivers.cargartabladri(registros)

        except Exception as error:
            print("Error al cargar alta los drivers", error)