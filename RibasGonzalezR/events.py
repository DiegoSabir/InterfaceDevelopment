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
            print("error in the events module, showExit ", error)



    def confirmExit(self):
        try:
            sys.exit()

        except Exception as error:
            print("error in the events module, confirmExit ", error)



    def cancelExit(self):
        try:
            var.exitWindow.hide()

        except Exception as error:
            print("error in the events module, cancelExit ", error)



    @staticmethod
    def openCalendar():
        try:
            var.calendar.show()

        except Exception as error:
            print("error opening calendar", error)