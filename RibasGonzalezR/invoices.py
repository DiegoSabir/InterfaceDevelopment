from PyQt6 import QtWidgets, QtCore, QtSql, QtGui

import connection
import customers
import events
import var


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
    def save_invoice():
        try:
            customer = var.ui.cmbIdCustomer.currentText()
            codigoCustomer = customer.split(" ")[0]
            registro = [codigoCustomer, var.ui.txtDateInvoice.text()]
            if events.Events.check_enroll_invoice():
                connection.Connection.enroll_invoice(registro)
                connection.Connection.select_invoice()

        except Exception as error:
            print('error en save_invoice from invoices', error)



    @classmethod
    def load_tab_invoices(cls, registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabInvoices.setRowCount(index + 1)
                var.ui.tabInvoices.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabInvoices.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabInvoices.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabInvoices.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabInvoices.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabInvoices.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargartablafac from invoices", error)



    @staticmethod
    def load_invoices():
        try:
            row = var.ui.tabInvoices.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.one_invoice(fila[0])
            datos = [var.ui.txtIdInvoice, var.ui.cmbIdCustomer, var.ui.txtDateInvoice]

            Invoices.clear()

            for i, dato in enumerate(datos):
                if i == 2:
                    name = connection.Connection.get_name_by_code(registro[2])
                    dato.setCurrentText(f"{registro[2]} {name}")
                else:
                    dato.setText(str(registro[i]))

            Invoices.cargartabviajes()

        except Exception as error:
            print("error en load_invoices from invoices", error)



    @staticmethod
    def cargartabviajes():
        try:
            var.ui.tabSale.setRowCount(0)

            registro = []

            query = QtSql.QSqlQuery()
            query.prepare('select * from sale where id_invoice_sale = :id_invoice')
            query.bindValue(':id_invoice', int(var.ui.txtIdInvoice.text()))

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

            Invoices.subiratablaviajes(registro)

        except Exception as error:
            print("error en cargartabviajes from invoices", error)