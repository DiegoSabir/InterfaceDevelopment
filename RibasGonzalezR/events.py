import os
import shutil
import xlrd
import xlwt
import connection
import var
import sys

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
