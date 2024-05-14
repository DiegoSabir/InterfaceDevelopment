import os
import shutil
import xlrd
import xlwt
import connection
import var
import sys
import re

from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui, QtSql

import zipfile
import locale

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Events:
    def showExit(self):
        try:
            var.exitWindow.show()

        except Exception as error:
            print("error en showExit from events", error)



    def confirmExit(self):
        try:
            sys.exit()

        except Exception as error:
            print("error en confirmExit  from events", error)



    def cancelExit(self):
        try:
            var.exitWindow.hide()

        except Exception as error:
            print("error en cancelExit from events", error)



    @staticmethod
    def showFireModify():
        try:
            var.dlgModifyFireWindow.show()

        except Exception as error:
            print("error en showFireModify from events", error)



    @staticmethod
    def confirmModify():
        try:
            var.calendar.show()

        except Exception as error:
            print("error en confirmModify from events", error)



    @staticmethod
    def cancelModify():
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
    def openCalendar():
        try:
            var.calendar.show()

        except Exception as error:
            print("error en openCalendar from events", error)



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

            # var.ui.txtPricePro.setText(str(locale.currency(float(var.ui.txtPricePro.text()))))

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



    @staticmethod
    def comprobarAltaFac():
        try:
            if not conexion.Conexion.existeDni(var.ui.txtCifCli.text()):
                if conexion.Conexion.comprobarclientebaja(var.ui.txtCifCli.text()):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
                    msg.setText('El cliente esta dado de baja')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.exec()
                    return False

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
                    msg.setText('El cliente no existe')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.exec()
                    return False

            elif var.ui.txtAltaFactura.text().strip() == "" or var.ui.txtCifCli.text().strip() == "" or var.ui.cbbConductorFactura.currentText().strip() == "":
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Faltan datos por cubrir')
                msg.exec()
                return False

            else:
                return True

        except Exception as error:
            print('Error al comprobar alta fac', error)
