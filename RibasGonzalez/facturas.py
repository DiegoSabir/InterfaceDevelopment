from PyQt6 import QtWidgets, QtCore, QtGui


import conexion
import clientes
import eventos
import var


class Facturas:
    def limpiarPanel3(self=None):
        try:
            listawidgets=[var.ui.lblcodbd2, var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2,
                          var.ui.txtmovil2, var.ui.lblValidarDNI2 ]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbCond.setCurrentText('')

        except Exception as error:
            print(str(error) + " en limpiarPanel3")



    def buscarClifact(self):
        try:
            dni = var.ui.txtcifcli.text()
            registro = conexion.Conexion.codCli(dni)
            clientes.Clientes.auxiliar(registro)
            codigo = var.ui.lblcodbd2.text()
            var.ui.rbtTodos2.setChecked(True)
            conexion.Conexion.mostrarClientes()
            clientes.Clientes.colorearFila(codigo)

        except Exception as error:
            print(str(error) + " en cargarcliente clientes")



    def cargaFechafact(qDate):
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtfechafact.setText(str(data))
            var.Altafact.hide()

        except Exception as error:
            print(str(error) + " en cargarfecha fact driver")



    def altafactura(self):
        try:
            registro=[var.ui.txtcifcli.text(), var.ui.txtfechafact.text(), var.ui.cmbCond.currentText().split('.')[0]]
            conexion.Conexion.altafacturacion(registro)

        except Exception as error:
            print("error altafact",error)



    def cargarTablaFacturas(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabFacturas.setRowCount(index + 1)
                var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablafacturas", error)



    def cargarFactura(self):
        try:
            Facturas.limpiarPanel3(self)
            row = var.ui.tabFacturas.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneFactura(fila[0])
            Facturas.auxiliar(registro)
            conexion.Conexion.cargarfacturas()
            Facturas.colorearFila(registro[0])

        except Exception as error:
            print(str(error) + " en cargarFactura")



    def auxiliar(registro):
        try:
            registro2 = conexion.Conexion.oneDriver(registro[3])
            driver = str()
            datos = [var.ui.lblcodfacturacion, var.ui.txtcifcli, var.ui.txtfechafact, var.ui.cmbCond]
            for i, dato in enumerate(datos):
                if i == 3:
                    dato.setCurrentText(str(driver))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")



    def colorearFila(numfactura):
        for fila in range(var.ui.tabFacturas.rowCount()):
            if var.ui.tabFacturas.item(fila, 0).text() == str(numfactura):
                for columna in range(var.ui.tabFacturas.columnCounter()):
                    item = var.ui.tabFacturas.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))