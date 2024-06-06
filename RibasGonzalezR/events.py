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
        try:
            var.exitWindow.show()

        except Exception as error:
            print("error en showExit from events", error)



    def confirm_exit(self):
        try:
            sys.exit()

        except Exception as error:
            print("error en confirmExit  from events", error)



    def cancel_exit(self):
        try:
            var.exitWindow.hide()

        except Exception as error:
            print("error en cancelExit from events", error)



    @staticmethod
    def show_fire_modify():
        try:
            var.dlgModifyFireWindow.show()

        except Exception as error:
            print("error en showFireModify from events", error)



    @staticmethod
    def confirm_modify():
        try:
            var.calendar.show()

        except Exception as error:
            print("error en confirmModify from events", error)



    @staticmethod
    def cancel_modify():
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Information')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText("Data Customer Modified")
            mbox.exec()
            var.dlgModifyFireWindow.hide()

        except Exception as error:
            print("error en cancelModify from events", error)



    @staticmethod
    def open_calendar():
        try:
            var.calendar.show()

        except Exception as error:
            print("error en openCalendar from events", error)



    @staticmethod
    def open_calendar_invoice():
        try:
            var.calendarInvoice.show()

        except Exception as error:
            print("error en open_calendar_invoice from events", error)



    @staticmethod
    def resizeCustomerTable():
        try:
            header = var.ui.tabCustomers.horizontalHeader()
            for i in range(var.ui.tabCustomers.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resizeCustomerTable from events", error)



    @staticmethod
    def capitalLetter():
        try:
            var.ui.txtSurname.setText(var.ui.txtSurname.text().title())
            var.ui.txtName.setText(var.ui.txtName.text().title())

        except Exception as error:
            print("error en capitalLetter from events", error)


    @staticmethod
    def blockTxtSurname():
        try:
            var.ui.txtSurname.setText("")
            var.ui.txtSurname.setEnabled(False)

        except Exception as error:
            print("error en blockTxtSurname from events", error)



    @staticmethod
    def unblockTxtSurname():
        try:
            var.ui.txtSurname.setEnabled(True)

        except Exception as error:
            print("error en unblockTxtSurname from events", error)



    @staticmethod
    def checkEmailFormat():
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
            print("Error en checkEmailFormat from events:", error)



    @staticmethod
    def checkPriceFormat():
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
            print("Error en checkPriceFormat from events", error)



    @staticmethod
    def resizeProductTable():
        try:
            header = var.ui.tabProducts.horizontalHeader()
            for i in range(var.ui.tabProducts.columnCount()):
                if i == 0:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resizeProductTable from events", error)



    @classmethod
    def resize_invoice_tab(cls):
        try:
            header = var.ui.tabInvoices.horizontalHeader()
            for i in range(var.ui.tabInvoices.columnCount()):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize_invoice_tab from events", error)



    @staticmethod
    def check_enroll_invoice():
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
        try:
            customers.Customers.clear()
            products.Products.clear_products()
            invoices.Invoices.clear_invoices()
            invoices.Invoices.clear_sale()

        except Exception as error:
            print("error en clear_all from events", error)