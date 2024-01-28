
import conexion
import clientes
import eventos
import var

from PyQt6 import QtWidgets, QtCore, QtGui

class Facturas:

    def limpiarPanel3(self=None):
        try:
            listawidgets=[var.ui.lblcodfacturacion, var.ui.txtcifcli, var.ui.txtfechafact, var.ui.txtkm]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbCond.setCurrentText('')
            var.ui.cmbProbVentas.setCurrentText('')
            var.ui.cmbProbVentas2.setCurrentText('')
            var.ui.cmbMuniVentas.setCurrentText('')
            var.ui.cmbMuniVentas2.setCurrentText('')
        except Exception as error:
            print(str(error) + " en limpiarpanel 3")
    def validarKm(self=None):
        try:
            km = var.ui.txtkm.text()
            numeros = "1234567890"
            var.ui.txtkm.setText(km)  # Corrección aquí
            if len(km):
                if len(km) != len([n for n in km if n in numeros]):
                    raise Exception
            else:
                raise Exception
        except Exception as error:
            eventos.Eventos.error("Aviso", "Los km deben ser de enteros")
            var.ui.txtkm.setText("")

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
                var.ui.tablaFacturas.setRowCount(index + 1)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablafacturas", error)

    def cargarFactura(self):
        try:

            Facturas.limpiarPanel3(self)
            row = var.ui.tablaFacturas.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneFactura(fila[0])
            Facturas.auxiliar(registro)
            conexion.Conexion.cargarfacturas()
            Facturas.colorearFila(registro[0])
            conexion.Conexion.viajesFactura(registro[0])
        except Exception as error:
            print(str(error) + " en cargarfact")
    def auxiliar(registro):
        try:
            registro2 = conexion.Conexion.oneDriver(registro[3])
            driver = str(registro2[0]) + "." + registro2[3]
            datos = [var.ui.lblcodfacturacion, var.ui.txtcifcli, var.ui.txtfechafact, var.ui.cmbCond]
            for i, dato in enumerate(datos):
                if i == 3:
                    dato.setCurrentText(str(driver))
                else:
                    dato.setText(str(registro[i]))
        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")

    def colorearFila(numfactura):
        for fila in range(var.ui.tablaFacturas.rowCount()):
            if var.ui.tablaFacturas.item(fila, 0).text() == str(numfactura):
                for columna in range(var.ui.tablaFacturas.columnCount()):
                    item = var.ui.tablaFacturas.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))

    def comprobarTarifa(self=None):
        try:
            provinciaOrigen = var.ui.cmbProbVentas.currentText()
            provinciaDestino = var.ui.cmbProbVentas2.currentText()
            localidadOrigen = var.ui.cmbMuniVentas.currentText()
            localidadDestino = var.ui.cmbMuniVentas2.currentText()

            if provinciaOrigen == provinciaDestino:
                var.ui.rbtProvincial.setChecked(True)
                if localidadOrigen == localidadDestino:
                    var.ui.rbtLocal.setChecked(True)
            else:
                var.ui.rbtNacional.setChecked(True)
        except Exception as error:
            print(error)

    def cargaTablaViajes(valores):
        try:
            var.ui.tabViajes.clearContents()
            subtotal=0.0
            index = 0
            for registro in valores:
                var.ui.tabViajes.setRowCount(index + 1)
                var.ui.tabViajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabViajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabViajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabViajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabViajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))

                totalViaje = round(float(registro[4]) * float(registro[3]), 2)
                subtotal +=totalViaje
                iva=totalViaje*0.21
                var.ui.lblsubtotal.setText(str(round(subtotal, 2)) + " €")
                var.ui.lbliva.setText(str(round(iva, 2)) + " €")
                var.ui.lbltotalfactura.setText(str(round(subtotal + iva, 2)) + " €")
                var.ui.tabViajes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(totalViaje)))
                subtotal= subtotal+totalViaje
                var.ui.tabViajes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                btn_borrar = QtWidgets.QPushButton()
                btn_borrar.setFixedSize(30, 28)
                btn_borrar.setIcon(QtGui.QIcon('./img/basura.png'))
                btn_borrar.clicked.connect(Facturas.borrarViaje)
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, btn_borrar)
                index += 1
        except Exception as error:
            print(str(error) + " en cargatablviajes facturas")



    def guardarViaje(self):
        try:
            if var.ui.lblcodfacturacion.text():
                if var.ui.txtkm.text() and str(var.ui.cmbMuniVentas.currentText()) != "" and str(var.ui.cmbMuniVentas2.currentText()) != "":
                    tarifa = '0.80'
                    if (var.ui.rbtLocal.isChecked()):
                        tarifa = '0.20'
                    elif(var.ui.rbtProvincial.isChecked()):
                        tarifa = '0.40'

                    viaje = [str(var.ui.lblcodfacturacion.text()), str(var.ui.cmbProbVentas.currentText()),
                             str(var.ui.cmbMuniVentas.currentText()), str(var.ui.cmbProbVentas2.currentText()),
                             str(var.ui.cmbMuniVentas2.currentText()), tarifa, str(var.ui.txtkm.text())]
                    conexion.Conexion.guardarViaje(viaje)
                    conexion.Conexion.viajesFactura(var.ui.lblcodfacturacion.text())
                else:
                    eventos.Eventos.error('Aviso',"Faltan campos obligatorios")
            else:
                eventos.Eventos.error('Aviso',"Selecciona primero una factura")

        except Exception as error:
            print(error)

    def cargarViaje(self):
        try:
            row = var.ui.tabViajes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneViajes(fila[0])

            provinciaOrigen, localidadOrigen = registro[2].split(" - ")
            provinciaDestino, localidadDestino = registro[3].split(" - ")

            var.ui.cmbProbVentas.setCurrentText(provinciaOrigen)
            var.ui.cmbMuniVentas.setCurrentText(localidadOrigen)
            var.ui.cmbProbVentas2.setCurrentText(provinciaDestino)
            var.ui.cmbMuniVentas2.setCurrentText(localidadDestino)

            var.ui.txtkm.setText(registro[5])

        except Exception as error:
            print(str(error) + " en cargarviaje")

    def borrarViaje(self):
        try:
            row = var.ui.tabViajes.selectedItems()
            fila = [dato.text() for dato in row]
            conexion.Conexion.borrarViaje(fila[0])
            conexion.Conexion.viajesFactura(var.ui.lblcodfacturacion.text())

        except Exception as error:
            print(error)


