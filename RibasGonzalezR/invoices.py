from PyQt6 import QtWidgets, QtCore, QtSql, QtGui

import connection
import customers
import events
import var

from customers import Customers


class Invoices:
    @staticmethod
    def clear():
        try:
            widgetList = [var.ui.txtIdInvoice, var.ui.cmbIdCustomer, var.ui.txtDateInvoice]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear from invoices", error)



    @staticmethod
    def load_date(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDateInvoice.setText(str(data))
            var.calendarInvoice.hide()

        except Exception as error:
            print("error en load_date from invoices", error)



    @staticmethod
    def open_calendar():
        try:
            var.calendarInvoice.show()

        except Exception as error:
            print("error en open_calendar from invoices", error)



    @staticmethod
    def load_invoices():
        try:
            row = var.ui.tabInvoices.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.oneInvoice(fila[0])

            datos = [var.ui.txtIdInvoice,
                     var.ui.cmbIdCustomer,
                     var.ui.txtDateInvoice]

            Invoices.clear()

            for i, dato in enumerate(datos):
                dato.setText(str(registro[i]))

            Invoices.load_tab_sales()

        except Exception as error:
            print("error en load_invoices from invoices", error)



    @classmethod
    def load_invoice_table(cls, registros):
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
            print("error en load_invoice_table from invoices", error)



    @staticmethod
    def save_invoice():
        try:
            customer = var.ui.cmbIdCustomer.currentText()
            codeCustomer = customer.split(" ")[0]
            register = [var.ui.txtDateInvoice.text(), codeCustomer]
            if events.Events.check_enroll_invoicing():
                connection.Connection.enroll_invoice(register)
                connection.Connection.select_invoice()

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

                tarifa = Invoices.cargartarifa()
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

                    Invoices.load_tab_sales()

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
    def load_tab_sales():
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

            Invoices.import_tab_sales(registro)

        except Exception as error:
            print("error en cargartabviajes ", error)



    def import_tab_sales(registros):
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
                botondel.setIcon(QtGui.QIcon('imagesg/basura.png'))
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, botondel)
                botondel.clicked.connect(connection.Connection.borrarviaje)

                index += 1
            var.ui.txtSubtotal.setText(str(subtotal))
            var.ui.txtIVA.setText('21%')
            var.ui.txtTotal.setText(str(round(float(subtotal + subtotal*21/100),2)))

        except Exception as error:
            print('error cargar dato en tabla', error)
