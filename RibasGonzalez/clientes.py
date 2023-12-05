from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var

class Clientes():

    @staticmethod
    def limpiapanel(self):
        try:
            listawidgets = [var.ui.lblcodbdCli, var.ui.txtDniCli, var.ui.txtDataCli, var.ui.txtRazonCli,
                            var.ui.txtDirCli, var.ui.txtMovil, var.ui.lblValidardniCli]

            for i in listawidgets:
                i.setText(None)

            var.ui.cmbProvCli.setCurrentText('')
            var.ui.cmbMuniCli.setCurrentText('')

            if var.ui.rbtAltaCli.isChecked():
                estado = 1
                conexion.Conexion.selectClientes(estado)
            else:
                registros = conexion.Conexion.mostrarclientes(self)
                Clientes.cargartablacli(registros)

        except Exception as error:
            print('Error al limpiar el panel cliente: ', error)



    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataCli.setText(str(data))
            return data
            var.calendar.hide()

        except Exception as error:
            print("Error al cargar fecha: ", error)



    def validarDNI(dni):
        try:
            dni = str(dni).upper() #poner mayúscula
            var.ui.txtDniCli.setText(str(dni))
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:           #comprueba que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidardniCli.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    var.ui.lblValidardniCli.setText('V')
                    return True
                else:
                    var.ui.lblValidardniCli.setStyleSheet('color:red;')    #y si no una X en color rojo
                    var.ui.lblValidardniCli.setText('X')
                    var.ui.txtDniCli.clear()
                    var.ui.txtDniCli.setFocus()
                    return False
            else:
                var.ui.lblValidardniCli.setStyleSheet('color:red;')
                var.ui.lblValidardniCli.setText('X')
                var.ui.txtDniCli.clear()
                var.ui.txtDniCli.setFocus()
                return False

        except Exception as error:
            print("Error en la validacion del dni", error)



    def altacliente(self):
        try:
            cliente = [var.ui.txtDniCli, var.ui.txtDataCli, var.ui.txtRazonCli,
                      var.ui.txtDirCli, var.ui.txtMovilCli]

            newcliente = []
            for i in cliente:
                newcliente.append(i.text().title())

            prov = var.ui.cmbProvCli.currentText()
            newcliente.insert(5, prov)
            muni = var.ui.cmbMuniCli.currentText()
            newcliente.insert(6, muni)



            valor = conexion.Conexion.guardarcli(newcliente)

            if valor == True:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Empleado dado de alta")
                mbox.exec()

            elif valor == False:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Asegúrese de que el conductor no existe")
                mbox.exec()

        except Exception as error:
            print("Error al dar de alta", error)



    def cargartablacli(registros):
        try:
            var.ui.tabClientes.clearContents()
            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index+1) #crea una fila
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("Error al cargar los datos en la tabla", error)



    def cargacliente(self):
        try:
            fila = var.ui.tabDrivers.selectedItems()
            row = [dato.text() for dato in fila]
            registro = conexion.Conexion.onecliente(row[0])
            Clientes.cargadatos(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente marcando en la tabla: ", error)



    def buscaCli(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codCli(dni)
            Clientes.cargadatos(registro)

            if var.ui.rbtTodosCli.isChecked():
                estado = 0
                conexion.Conexion.selectClientes(estado)
            elif var.ui.rbtAltaCli.isChecked():
                estado = 1
                conexion.Conexion.selectClientes(estado)
            elif var.ui.rbtBajaCli.isChecked():
                estado = 2
                conexion.Conexion.selectClientes(estado)

            codigo = var.ui.lblcodbdCli.text()
            for fila in range(var.ui.tabClientes.rowCount()):
                if var.ui.tabClientes.item(fila, 0).text() == str(codigo):
                    for columna in range(var.ui.tabClientes.columnCount()):
                        item = var.ui.tabClientes.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))

        except Exception as error:
            print(error, "al buscar datos de un cliente")



    def cargadatos(registro):
        try:
            datos = [var.ui.lblcodbdCli, var.ui.txtDniCli, var.ui.txtDataCli, var.ui.txtRazonCli,
                     var.ui.txtDirCli, var.ui.cmbProvCli, var.ui.cmbMuniCli, var.ui.txtMovilCli]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))


        except Exception as error:
            print("Error al cargar los datos en el panel de gestión", error)


    """
        def modifCli(self):
        try:
            cliente = [var.ui.lblcodbdCli, var.ui.txtDniCli, var.ui.txtDataCli, var.ui.txtRazonCli,
                      var.ui.txtDirCli, var.ui.txtMovilCli]

            modifcliente = []
            for i in cliente:
                modifcliente.append(i.text().title())

            prov = var.ui.cmbProvCli.currentText()
            modifcliente.insert(6, prov)
            muni = var.ui.cmbMuniCli.currentText()
            modifcliente.insert(7, muni)

            conexion.Conexion.modifCliente(modifcliente)

        except Exception as error:
            print("Error al modificar cliente", error)
    """




    def borrarCliente(self):
        try:
            dni = var.ui.txtDniCli.text()
            conexion.Conexion.borrarCli(dni)
            conexion.Conexion.selectClientes(1)

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El cliente no existe o no se puede borrar")
            mbox.exec()



    def selEstado(self):
        if var.ui.rbtTodosCli.isChecked():
            estado = 0
            conexion.Conexion.selectClientes(estado)

        elif var.ui.rbtAltaCli.isChecked():
            estado = 1
            conexion.Conexion.selectClientes(estado)

        elif var.ui.rbtBajaCli.isChecked():
            estado = 2
            conexion.Conexion.selectClientes(estado)