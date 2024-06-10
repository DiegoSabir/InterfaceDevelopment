import os
import shutil
import xlrd
import xlwt
import connection
import customers
import invoices
import products
import var
import sys
import re

from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui, QtSql

import zipfile
import locale

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Events:
    def show_exit(self):
        """
        Muestra la ventana de confirmación de salida.

        :return: None
        """
        try:
            var.exitWindow.show()

        except Exception as error:
            print("error en show_exit from events", error)



    def confirm_exit(self):
        """
        Confirma la salida de la aplicación.

        :return: None
        """
        try:
            sys.exit()

        except Exception as error:
            print("error en confirm_exit from events", error)



    def cancel_exit(self):
        """
        Cancela la salida de la aplicación y oculta la ventana de confirmación de salida.

        :return: None
        """
        try:
            var.exitWindow.hide()

        except Exception as error:
            print("error en cancel_exit from events", error)



    @staticmethod
    def show_fire_modify():
        """
        Muestra la ventana de modificación de baja.

        :return: None
        """
        try:
            var.dlgModifyFireWindow.show()

        except Exception as error:
            print("error en show_fire_modify from events", error)



    @staticmethod
    def confirm_modify():
        """
        Muestra el calendario para seleccionar una fecha.

        :return: None
        """
        try:
            var.calendar.show()

        except Exception as error:
            print("error en confirm_modify from events", error)



    @staticmethod
    def cancel_modify():
        """
        Confirma la modificación de los datos del cliente y oculta la ventana de modificación de baja.

        :return: None
        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Information')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText("Data Customer Modified")
            mbox.exec()
            var.dlgModifyFireWindow.hide()

        except Exception as error:
            print("error en cancel_modify from events", error)



    @staticmethod
    def open_calendar():
        """
        Muestra el calendario para seleccionar una fecha.

        :return: None
        """
        try:
            var.calendar.show()

        except Exception as error:
            print("error en open_calendar from events", error)



    @staticmethod
    def open_calendar_invoice():
        """
        Muestra el calendario para seleccionar una fecha en las facturas.

        :return: None
        """
        try:
            var.calendarInvoice.show()

        except Exception as error:
            print("error en open_calendar_invoice from events", error)



    @staticmethod
    def resize_customer_table():
        """
        Ajusta el tamaño de las columnas de la tabla de clientes en la interfaz de usuario.

        :return: None
        """
        try:
            header = var.ui.tabCustomers.horizontalHeader()
            for i in range(var.ui.tabCustomers.columnCount()):
                if i == 0 or i == 3 or i == 4 or i == 5:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2 or i == 6:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize_customer_table from events", error)



    @staticmethod
    def capital_letter():
        """
        Convierte la primera letra de los campos de apellido y nombre en mayúscula.

        :return: None
        """
        try:
            var.ui.txtSurname.setText(var.ui.txtSurname.text().title())
            var.ui.txtName.setText(var.ui.txtName.text().title())

        except Exception as error:
            print("error en capital_letter from events", error)



    @staticmethod
    def block_txt_surname():
        """
        Limpia y deshabilita el campo de texto del apellido.

        :return: None
        """
        try:
            var.ui.txtSurname.setText("")
            var.ui.txtSurname.setEnabled(False)

        except Exception as error:
            print("error en block_txt_surname from events", error)



    @staticmethod
    def unblock_txt_surname():
        """
        Habilita el campo de texto del apellido.

        :return: None
        """
        try:
            var.ui.txtSurname.setEnabled(True)

        except Exception as error:
            print("error en unblock_txt_surname from events", error)



    @staticmethod
    def check_email_format():
        """
        Verifica el formato del correo electrónico y muestra una advertencia si es inválido.

        :return: None
        """
        try:
            email = var.ui.txtEmail.text()
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, email):
                var.ui.txtEmail.setText(email)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Invalid Email Format")
                mbox.exec()
                var.ui.txtEmail.setText("")
                var.ui.txtEmail.setFocus()

        except Exception as error:
            print("Error en check_email_format from events:", error)



    @staticmethod
    def check_price_format():
        """
        Verifica el formato del precio y muestra una advertencia si es incorrecto.

        :return: None
        """
        try:
            price = var.ui.txtPricePro.text()
            price = price.replace('€', '').strip()
            price = price.replace(',', '.')
            var.ui.txtPricePro.setText(price)
            priceNumber = float(price)

            if priceNumber < 0.00:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Warning')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Incorrect Price Format (000.00)')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Ok')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtPricePro.setText("")
                var.ui.txtPricePro.setFocus()

        except Exception as error:
            print("Error en check_price_format from events", error)



    @staticmethod
    def resize_product_table():
        """
        Ajusta el tamaño de las columnas de la tabla de productos en la interfaz de usuario.

        :return: None
        """
        try:
            header = var.ui.tabProducts.horizontalHeader()
            for i in range(var.ui.tabProducts.columnCount()):
                if i == 0:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize_product_table from events", error)



    @classmethod
    def resize_invoice_tab(cls):
        """
        Ajusta el tamaño de las columnas de la tabla de facturas en la interfaz de usuario.

        :return: None
        """
        try:
            header = var.ui.tabInvoices.horizontalHeader()
            for i in range(var.ui.tabInvoices.columnCount()):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize_invoice_tab from events", error)



    @staticmethod
    def check_enroll_invoice():
        """
        Verifica que los campos de la factura no estén vacíos y muestra una advertencia si faltan datos.

        :return: True si los datos son válidos, False en caso contrario.
        """
        try:
            if var.ui.cmbIdCustomer.currentText().strip() == "" or var.ui.txtDateInvoice.text().strip() == "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Warning')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Missing data')
                msg.exec()
                return False

            else:
                return True

        except Exception as error:
            print('error en check_enroll_invoice from events', error)



    @staticmethod
    def resize_sale_tab():
        """
        Ajusta el tamaño de las columnas de la tabla de ventas en la interfaz de usuario.

        :return: None
        """
        try:
            header = var.ui.tabSale.horizontalHeader()
            for i in range(var.ui.tabSale.columnCount()):
                if i == 0 or i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize_sell_tab from events", error)


    @staticmethod
    def clear_all():
        """
        Limpia todos los datos de los clientes, productos, facturas y ventas en la interfaz de usuario.

        :return: None
        """
        try:
            customers.Customers.clear()
            products.Products.clear_products()
            invoices.Invoices.clear_invoices()
            invoices.Invoices.clear_sale()

        except Exception as error:
            print("error en clear_all from events", error)
