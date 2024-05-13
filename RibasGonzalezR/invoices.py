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
    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDateInvoice.setText(str(data))
            var.calendarFacturacion.hide()

        except Exception as error:
            print("error en cargarFecha from invoices", error)



    @staticmethod
    def abrirCalendar():
        """
        Método estático para mostrar el calendario de facturación.
        """
        try:
            var.calendarFacturacion.show()

        except Exception as error:
            print("error en abrirCalendar from invoices", error)



    @staticmethod
    def cargarfacturas():
        """
        Método estático para cargar las facturas en la interfaz gráfica.
        """
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