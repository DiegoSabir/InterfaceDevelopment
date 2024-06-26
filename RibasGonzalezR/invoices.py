from PyQt6 import QtWidgets, QtCore, QtSql, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QComboBox, QTableWidgetItem, QSpinBox, QLabel

import connection
import customers
import events
import var


class Invoices:
    @staticmethod
    def clear_invoices():
        """
        Limpia los campos de información de la factura en la interfaz de usuario.

        :return: None
        """
        try:
            widgetList = [var.ui.txtIdInvoice, var.ui.txtDateInvoice]

            var.ui.cmbIdCustomer.setCurrentIndex(0)
            for i in widgetList:
                i.clear()

        except Exception as error:
            print("error en clear_invoices from invoices", error)



    @staticmethod
    def load_date(qDate):
        """
        Carga una fecha seleccionada en el campo de fecha de la factura y oculta el calendario.

        :param qDate: Objeto QDate que representa la fecha a cargar.
        :return: None
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDateInvoice.setText(str(data))
            var.calendarInvoice.hide()

        except Exception as error:
            print("error en load_date from invoices", error)



    @staticmethod
    def open_calendar():
        """
        Muestra el calendario para seleccionar una fecha.

        :return: None
        """
        try:
            var.calendarInvoice.show()

        except Exception as error:
            print("error en open_calendar from invoices", error)



    def enroll_invoice(self):
        """
        Registra una nueva factura en la base de datos.

        :return: None
        """
        try:
            date = var.ui.txtDateInvoice.text().strip()
            customer = var.ui.cmbIdCustomer.currentText().strip()

            if not date or not customer:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Missing data")
                mbox.exec()

            else:
                codigoCustomer = customer.split(" ")[0]
                registro = [codigoCustomer, date]
                connection.Connection.save_invoice(registro)

        except Exception as error:
            print("error en enroll_invoice from invoices", error)



    def load_invoice_tab(registros):
        """
        Carga los datos de las facturas en la tabla de la interfaz de usuario.

        :param registros: Lista de registros de facturas a cargar.
        :return: None
        """
        try:
            var.ui.tabInvoices.setRowCount(len(registros))
            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabInvoices.setItem(index, col_index, item)

        except Exception as error:
            print("error en load_invoice_tab from invoices:", error)



    @staticmethod
    def load_invoice():
        """
        Carga los datos de la factura seleccionada en los campos de información de la interfaz de usuario.

        :return: None
        """
        try:
            Invoices.clear_invoices()
            selected_row = var.ui.tabInvoices.currentRow()

            if selected_row != -1:
                sale = var.ui.tabInvoices.item(selected_row, 0).text()
                registro = connection.Connection.one_invoice(sale)

                if registro:
                    datos = [var.ui.txtIdInvoice, var.ui.cmbIdCustomer, var.ui.txtDateInvoice]

                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit) or isinstance(dato, QLabel):
                            dato.setText(str(value))

                        elif isinstance(dato, QComboBox):
                            dato.setCurrentIndex(int(value))

                invoice = var.ui.txtIdInvoice.text()
                var.ui.txtIdInvoiceSale.setText(invoice)
                connection.Connection.load_sale(invoice)

        except Exception as error:
            print("error en load_invoice from invoices: ", error)



    @staticmethod
    def enroll_sale():
        """
        Registra una nueva venta en la base de datos.

        :return: None
        """
        try:
            invoice = var.ui.txtIdInvoiceSale.text().strip()
            product = var.ui.cmbIdProductSale.currentText().strip()
            idProdu = product.split(". ")[0]
            quantity = var.ui.spQuantitySale.value()

            if not invoice or not product or quantity <= 0:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Missing data")
                mbox.exec()

            else:
                registro = [invoice, idProdu, quantity]
                connection.Connection.save_sale(registro)

        except Exception as error:
            print("error en enroll_sale from invoices: ", error)



    def load_sale_tab(registros):
        """
        Carga los datos de las ventas en la tabla de la interfaz de usuario y calcula el subtotal, IVA y total.

        :param registros: Lista de registros de ventas a cargar.
        :return: None
        """
        try:
            subtotal = 0.0
            var.ui.tabSale.setRowCount(len(registros))

            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    if col_index == 2:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                    else:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabSale.setItem(index, col_index, item)

                total = round(float(registro[4]) * float(registro[3]), 2)
                subtotal += total
                iva = subtotal * 0.21
                var.ui.txtSubtotal.setText(f'{subtotal:.2f} €')
                var.ui.txtIVA.setText(f'{iva:.2f} €')
                var.ui.txtTotal.setText(f'{subtotal + iva:.2f} €')

        except Exception as error:
            print("error en load_sale_tab from invoices: ", error)



    @staticmethod
    def load_sale():
        """
        Carga los datos de la venta seleccionada en los campos de información de la interfaz de usuario.

        :return: None
        """
        try:
            Invoices.clear_sale()

            selected_row = var.ui.tabSale.currentRow()

            if selected_row != -1:
                sale = var.ui.tabSale.item(selected_row, 0).text()
                registro = connection.Connection.one_sale(sale)

                datos = [var.ui.txtIdSale, var.ui.txtIdInvoiceSale, var.ui.cmbIdProductSale, var.ui.spQuantitySale]

                for i, dato in enumerate(datos):
                    if i == 0 or i == 1:
                        dato.setText(str(registro[i]))

                    if i == 2:
                        dato.setCurrentIndex(int(registro[i]))

                    if i == 3:
                        dato.setValue(int(registro[i]))

        except Exception as error:
            print("error en load_sale from invoices: ", error)



    def modify_sale(self):
        """
        Modifica los datos de una venta en la base de datos.

        :return: None
        """
        try:
            sale = var.ui.txtIdSale.text().strip()
            product = var.ui.cmbIdProductSale.currentText().strip()
            idProdu = product.split(". ")[0]
            quantity = var.ui.spQuantitySale.value()

            datos = [sale, idProdu, quantity]

            connection.Connection.modify_sale(datos)
            connection.Connection.load_sale(sale)

        except Exception as error:
            print("error en modify_sale from invoices", error)



    @staticmethod
    def clear_sale():
        """
        Limpia los campos de información de la venta en la interfaz de usuario.

        :return: None
        """
        try:
            sale = [var.ui.txtIdSale, var.ui.txtIdInvoiceSale]
            var.ui.cmbIdProductSale.setCurrentIndex(0)
            var.ui.spQuantitySale.setValue(0)

            for i in sale:
                i.setText("")

        except Exception as error:
            print("error en clear_sale from invoices", error)
