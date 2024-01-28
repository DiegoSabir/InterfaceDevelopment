
from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
import conexion
import var
import eventos
class Clientes():
    def limpiarPanel2(self=None):
        try:
            listawidgets=[var.ui.lblcodbd2, var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2,
                          var.ui.txtmovil2, var.ui.lblValidarDNI2 ]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbProv2.setCurrentText('')
            var.ui.cmbMuni2.setCurrentText('')
        except Exception as error:
            print(str(error) + " en validar drivers")

    def buscarCliente(self):
        try:
            dni = var.ui.txtDNI2.text()
            registro = conexion.Conexion.codCli(dni)
            Clientes.auxiliar(registro)
            codigo = var.ui.lblcodbd2.text()
            var.ui.rbtTodos2.setChecked(True)
            conexion.Conexion.mostrarClientes()
            Clientes.colorearFila(codigo)
        except Exception as error:
            print(str(error) + " en cargarcliente clientes")
    def cargarCliente(self):
        try:
            Clientes.limpiarPanel2()
            row = var.ui.tabClientes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneCliente(fila[0])
            Clientes.auxiliar(registro)
            conexion.Conexion.mostrarClientes()
            Clientes.colorearFila(registro[0])
        except Exception as error:
            print(str(error) + " en cargar clientes clientes")

    def auxiliar(registro):
        try:
            datos = [var.ui.lblcodbd2, var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2,
                     var.ui.cmbProv2, var.ui.cmbMuni2]
            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")
    def colorearFila(codigo):
        for fila in range(var.ui.tabClientes.rowCount()):
            if var.ui.tabClientes.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tabClientes.columnCount()):
                    item = var.ui.tabClientes.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def cargarTablaClientes(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablaclientes", error)

    def validarDNI2(dni):
        try:
            var.ui.txtDNI2.setText(dni)  # Corrección aquí
            tabla = "TRWAGMYFPDXBNJZSKVHLCKE"
            digExt = "XYZ"
            reempDigExt = {"X": '0', "Y": '1', "Z": '2'}
            numeros = "1234567890"
            imgCorrecto = QPixmap('img/tickcirclehd_106142.ico')
            imgIncorrecto = QPixmap('img/crosscircleregular_106260.ico')

            if len(dni) == 9:
                digControl = dni[8]
                dni = dni[:8]
                if dni[0] in digExt:
                    dni = dni.replace(dni[0], reempDigExt[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == digControl:
                    var.ui.lblValidarDNI2.setPixmap(imgCorrecto)
                    var.ui.txtfecha.setFocus()
                    return True
                else:
                    var.ui.lblValidarDNI2.setPixmap(imgIncorrecto)
                    var.ui.txtDNI2.setText(None)
                    var.ui.txtDNI2.setFocus()
                    return False
            else:
                var.ui.lblValidarDNI2.setPixmap(imgIncorrecto)
                var.ui.txtDNI2.setText(None)
                var.ui.txtDNI2.setFocus()
                return False
        except Exception as error:
            print(str(error) + " en validar drivers")


    def validarMovil2(self=None):
        try:
            movil = var.ui.txtmovil2.text()
            numeros = "1234567890"
            var.ui.txtmovil2.setText(movil)  # Corrección aquí
            if len(movil) == 9:
                digControl = movil[:9]
                if len(movil) != len([n for n in movil if n in numeros]) == digControl:
                    raise Exception
            else:
                raise Exception
        except Exception as error:
            eventos.Eventos.error("Aviso", "El telefono debe ser una cadena de 9 numeros enteros")
            var.ui.txtmovil2.setText("")

    def altaCliente(self):
        try:
            dni = var.ui.txtDNI2.text()
            if conexion.Conexion.verificarCli(dni):
                conexion.Conexion.volverDarAlta2(dni)
                Clientes.limpiarPanel2(self)
                conexion.Conexion.mostrarClientes()
            else:
                if not all([var.ui.txtDNI2.text(), var.ui.txtsocial.text(), var.ui.txtmovil2.text()]):
                    eventos.Eventos.mensaje("Aviso", "Faltan datos obligatorios")
                    return
                cliente = [
                    var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2
                ]
                newCliente = []
                for i in cliente:
                    newCliente.append(i.text().title())

                prov = var.ui.cmbProv2.currentText()
                newCliente.insert(3, prov)
                muni = var.ui.cmbMuni2.currentText()
                newCliente.insert(4, muni)
                valor=conexion.Conexion.guardarcli(newCliente)
                if valor==True:
                    eventos.Eventos.mensaje("Aviso", "El cliente fue añadido con exito")
                    conexion.Conexion.mostrardriver()
                elif valor == False:
                    eventos.Eventos.error("Aviso", "No se ha podido dar de alta")

        except Exception as error:
            print(str(error) + " en altacliente clientes")
    def modifCli(self):
        try:
            driver=[var.ui.lblcodbd2,var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2]
            modifCliente=[]
            for i in driver:
                modifCliente.append(i.text().title())
            prov = var.ui.cmbProv2.currentText()
            modifCliente.insert(4,prov)
            muni = var.ui.cmbMuni2.currentText()
            modifCliente.insert(5,muni)
            conexion.Conexion.modifCliente(modifCliente)
        except Exception as error:
            print(error, " en modifcli")

    def borraCli(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.Bajacli.hide()
            dni = var.ui.txtDNI2.text()
            conexion.Conexion.borrarCli(dni, str(data))
            conexion.Conexion.mostrarClientes()
        except Exception as error:
            eventos.Eventos.error("Aviso", "El cliente no existe o no se puede borrar")