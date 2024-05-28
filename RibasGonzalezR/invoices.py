from PyQt6 import QtWidgets, QtCore, QtSql, QtGui

import connection
import customers
import events
import var

from customers import Customers


class Invoices:
    @staticmethod
    def burcaclifac():
        try:
            pass

        except Exception as error:
            print("error en burcaclifac from invoices", error)



    @staticmethod
    def load_date(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDateInvoice.setText(str(data))
            var.calendarInvoice.hide()

        except Exception as error:
            print("error en cargarFecha from invoices", error)



    @staticmethod
    def open_calendar():
        try:
            var.calendarInvoice.show()

        except Exception as error:
            print("error en abrirCalendar from invoices", error)



    @staticmethod
    def load_invoices():
        try:
            row = var.ui.tabInvoices.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.oneInvoice(fila[0])

            datos = [var.ui.txtIdInvoice,
                     var.ui.cmbIdCustomer,
                     var.ui.txtDateInvoice]

            Customers.clear()

            for i, dato in enumerate(datos):
                if i == 3:
                    apel = connection.Connection.getSurnameByCode(registro[3])
                    dato.setCurrentText(f"{registro[3]} {apel}")
                else:
                    dato.setText(str(registro[i]))

            Invoices.loadTabSales()

        except Exception as error:
            print("error en cargarfacturas from invoices", error)



    @classmethod
    def cargartablafac(cls, registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabInvoices.setRowCount(index + 1)
                var.ui.tabInvoices.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabInvoices.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabInvoices.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabInvoices.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargartablafac from invoices", error)



    @staticmethod
    def guardarFac():
        try:
            customer = var.ui.cbbConductorFactura.currentText()
            codeCustomer = customer.split(" ")[0]
            registro = [var.ui.txtCifCli.text(), var.ui.txtAltaFactura.text(), codeCustomer]
            if events.Events.comprobarAltaFac():
                connection.Connection.altaFacturacion(registro)
                connection.Connection.selectFactura()

        except Exception as error:
            print('Error en guardarFac from invoices', error)



    @staticmethod
    def guardarViaje():
        """
        Método estático para guardar un viaje.
        """
        try:

            if(var.ui.txtKm.text().strip() == "" or var.ui.cmbMuniOrigen.currentText().strip() == "" or var.ui.cmbMuniDestino.currentText().strip() == "" or var.ui.lblNumFactura.text().strip() == ""):

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan datos.")
                mbox.exec()

            else:

                tarifa = Facturas.cargartarifa()
                registro = [var.ui.lblNumFactura.text(), var.ui.cmbMuniOrigen.currentText(), var.ui.cmbMuniDestino.currentText(), tarifa, var.ui.txtKm.text()]

                query = QtSql.QSqlQuery()
                query.prepare('insert into viajes (factura, origen, destino, tarifa, km) values (:factura, :muniOrg, :muniDest, :tarifa, :km)')
                query.bindValue(':factura',int(registro[0]))
                query.bindValue(':muniOrg',str(registro[1]))
                query.bindValue(':muniDest',str(registro[2]))
                query.bindValue(':tarifa',str(registro[3]))
                query.bindValue(':km',str(registro[4]))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Viaxe gardado con exito.")
                    mbox.exec()

                    facturas.Facturas.cargartabviajes()

                else:
                    print(query.lastError())
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Viaxe non gardado.")
                    mbox.exec()

        except Exception as error:
            print("Error en guardarviaje ", error)



    @staticmethod
    def cargartarifa():
        """
        Método estático para cargar la tarifa del viaje.
        """
        try:
            if var.ui.rbtnNacional.isChecked():
                tarifa = 0.8

            elif var.ui.rbtnLocal.isChecked():
                tarifa = 0.2

            else:
                tarifa = 0.4

            return tarifa

        except Exception as error:
            print("error en cargartarifa ", error)



    @staticmethod
    def cargartabviajes():
        """
        Método estático para cargar los viajes en la tabla.
        """
        try:

            var.ui.tabViajes.setRowCount(0)

            registro = []

            query = QtSql.QSqlQuery()
            query.prepare('select * from viajes where factura = :factura')
            query.bindValue(':factura',int(var.ui.lblNumFactura.text()))

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

            facturas.Facturas.subiratablaviajes(registro)

        except Exception as error:
            print("error en cargartabviajes ", error)



    def subiratablaviajes(registros):

        try:
            index = 0
            subtotal = 0
            for registro in registros:
                var.ui.tabViajes.setRowCount(index + 1)
                var.ui.tabViajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabViajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabViajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabViajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabViajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                total = float(registro[4])*float(registro[5])
                subtotal += total
                var.ui.tabViajes.setItem(index, 5, QtWidgets.QTableWidgetItem('%.2f'%total))

                botondel = QtWidgets.QPushButton()
                botondel.setFixedSize(40, 28)
                botondel.setIcon(QtGui.QIcon('img/basura.ico'))
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, botondel)
                botondel.clicked.connect(conexion.Conexion.borrarviaje)

                index += 1
            var.ui.txtSubtotal.setText(str(subtotal))
            var.ui.txtIVA.setText('21%')
            var.ui.txtTotal.setText(str(round(float(subtotal + subtotal*21/100),2)))

        except Exception as error:
            print('error cargar dato en tabla', error)



    @staticmethod
    def cargarrbtn():
        """
        Método estático para cargar los botones según las opciones seleccionadas.
        """
        if var.ui.cmbMuniOrigen.currentText() != "" and var.ui.cmbMuniDestino.currentText() != "":

            if var.ui.cmbMuniOrigen.currentText() == var.ui.cmbMuniDestino.currentText():

                var.ui.rbtnLocal.setChecked(True)

            elif var.ui.cmbProvOrigen.currentText() == var.ui.cmbProvDestino.currentText():

                var.ui.rbtnProvincial.setChecked(True)

            else:
                var.ui.rbtnNacional.setChecked(True)



    @staticmethod
    def cargarViajes():
        """
        Método estático para cargar los viajes seleccionados en la interfaz gráfica.
        """
        try:

            row = var.ui.tabViajes.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneviaje(fila[0])

            datos = [var.ui.cmbProvOrigen, var.ui.cmbMuniOrigen, var.ui.cmbProvDestino, var.ui.cmbMuniDestino,
                     var.ui.txtKm]

            muniOrg = registro[2]
            muniDest = registro[3]

            provOrg = facturas.Facturas.getProvByMuni(muniOrg)
            provDest = facturas.Facturas.getProvByMuni(muniDest)

            datos[0].setCurrentText(provOrg)
            datos[1].setCurrentText(muniOrg)
            datos[2].setCurrentText(provDest)
            datos[3].setCurrentText(muniDest)
            datos[4].setText(registro[5])

        except Exception as error:
            print("error ao cargar viaxe seleccionado ", error)



    def getProvByMuni(muni : str):
        """
        Retorna una provincia segun idprov del municipio pasado como argumento

        :param muni:
        :type str:
        :return prov:
        :rtype str:
        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias where idprov = (select idprov from municipios where municipio = :mun)')
            query.bindValue(':mun', str(muni))

            if query.exec():
                query.next()
                return query.value(0)

            else:
                print(query.lastError())

        except Exception as error:
            print('error en getProvByMuni ', error)



    @staticmethod
    def buscaclifac():
        """
        Muestra solo las facturas de un cliente
        """
        try:
            dni = str(var.ui.txtCifCli.text())
            dni = dni.upper()
            drivers.Drivers.limpiarPanel()
            var.ui.txtCifCli.setText(dni)
            registros = conexion.Conexion.viajesCliente(dni)
            if len(registros) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('No se encontró ningún empleado')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.exec()
            else:
                Facturas.cargartablafac(registros)
        except Exception as error:
            print("buscaclifac: ", error)



    @staticmethod
    def modifviaje():
        """

        Actualiza la información del registro de un viaje

        :return:
        :rtype:
        """
        try:

            registro = []
            registro = var.ui.tabViajes.selectedItems()
            index = registro[0].text()
            print(index)

            if var.ui.cmbMuniOrigen.currentText().strip() == "" or var.ui.cmbProvOrigen.currentText().strip() == "" or var.ui.cmbMuniDestino.currentText().strip() == "" or var.ui.txtKm.text().strip() == "" or registro == [] :

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Non se pode modificar\nxa que faltan datos")
                mbox.exec()

            else:

                query = QtSql.QSqlQuery()
                query.prepare("update viajes set origen = :origen, destino = :destino, km = :km, tarifa = :tarifa where idviaje = :id")
                query.bindValue(':origen', var.ui.cmbMuniOrigen.currentText())
                query.bindValue(':destino', var.ui.cmbMuniDestino.currentText())
                query.bindValue(':km', var.ui.txtKm.text())
                query.bindValue(':tarifa', Facturas.cargartarifa())
                query.bindValue(':id', index)

                if query.exec():

                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Viaxe modificada!")
                    mbox.exec()

                    Facturas.cargartabviajes()

                else:

                    print(query.lastError().text())

                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Non se pode modificar\npor un erro:\n")
                    mbox.exec()

        except Exception as error:
            print("Error en modifviaje ", error)



    @staticmethod
    def borrarFactura():
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where numfac = :idfac')
            query.bindValue(':idfac', int(var.ui.lblNumFactura.text()))

            if eventos.Eventos.pedirConfirmacion("¿Quieres eliminar la factura?"):

                if query.exec():
                    query.next()

                    eventos.Eventos.invocarMesageBox("Factura eliminada")
                else:
                    eventos.Eventos.invocarMesageBox("Error al eliminar la factura")
                    print(query.lastError().text())

            conexion.Conexion.selectFactura()
            drivers.Drivers.limpiarPanel()
            var.ui.tabViajes.setRowCount(0)

        except Exception as error:
            print('Error al borrar factura')
