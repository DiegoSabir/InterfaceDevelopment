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
        try:
            widgetList = [var.ui.txtIdInvoice, var.ui.cmbIdCustomer, var.ui.txtDateInvoice]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear_invoices from invoices", error)



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



    def enroll_invoice(self):
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
                codCli = customer.split(" ")[0]
                registro = [codCli, date]
                connection.Connection.save_invoice(registro)

        except Exception as error:
            print("error en enroll_invoice from invoices", error)



    def load_invoice_tab(registros):
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
                            # Busca el índice del valor en el QComboBox y lo selecciona
                            index = dato.findText(value, QtCore.Qt.MatchFlag.MatchFixedString)
                            if index >= 0:
                                dato.setCurrentIndex(index)

                            else:
                                # Si no se encuentra, se puede agregar el valor y seleccionarlo
                                dato.addItem(value)
                                dato.setCurrentIndex(dato.count() - 1)

                invoice = var.ui.txtIdInvoice.text()
                var.ui.txtIdInvoiceSale.setText(invoice)
                connection.Connection.load_sale(invoice)

        except Exception as error:
            print("error en load_invoice from invoices: ", error)



    @staticmethod
    def enroll_sale():
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
        try:
            subtotal = 0.0
            var.ui.tabSale.setRowCount(len(registros))

            for index, registro in enumerate(registros):
                for col_index, value in enumerate(registro):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabSale.setItem(index, col_index, item)

                total = round(float(registro[4]) * float(registro[3]), 2)
                subtotal = subtotal + total
                iva = subtotal * 0.21
                var.ui.txtSubtotal.setText(str('{:.2f}'.format(round(subtotal, 2))) + " €")
                var.ui.txtIVA.setText(str('{:.2f}'.format(round(iva, 2))) + " €")
                var.ui.txtTotal.setText(str('{:.2f}'.format(round(subtotal + iva, 2))) + " €")

        except Exception as error:
            print("error en load_sale_tab from invoices: ", error)



    @staticmethod
    def load_sale():
        try:
            Invoices.clear_sale()

            selected_row = var.ui.tabSale.currentRow()

            if selected_row != -1:
                sale = var.ui.tabSale.item(selected_row, 0).text()
                registro = connection.Connection.one_sale(sale)

                if registro:
                    datos = [var.ui.txtIdSale, var.ui.txtIdInvoiceSale, var.ui.cmbIdProductSale, var.ui.spQuantitySale]

                    for dato, value in zip(datos, registro):
                        if isinstance(dato, QLineEdit):
                            dato.setText(str(value))

                        elif isinstance(dato, QComboBox):
                            dato.setCurrentIndex(int(value))

                        elif isinstance(dato, QSpinBox):
                            dato.setValue(int(value))

        except Exception as error:
            print("error en load_sale from invoices: ", error)



    def modify_sale(self):
        try:
            sale = var.ui.txtIdSale.text().strip()
            product = var.ui.cmbIdProductSale.currentText().strip()
            idProdu = product.split(". ")[0]
            quantity = var.ui.spQuantitySale.value()

            datos = [sale, idProdu, quantity]

            connection.Connection.modify_sale(datos)

            Invoices.load_sale()

        except Exception as error:
            print("error en modify_sale from invoices", error)



    @staticmethod
    def clear_sale():
        try:
            sale = [var.ui.txtIdSale, var.ui.txtIdInvoiceSale]
            var.ui.cmbIdProductSale.setCurrentIndex(0)
            var.ui.spQuantitySale.setValue(0)

            for i in sale:
                i.setText("")

        except Exception as error:
            print(error)
