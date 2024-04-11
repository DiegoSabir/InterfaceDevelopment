from auxiliar import *
from datetime import datetime

import locale
import os.path
import xlrd
import customer
import connection
import sys
import zipfile
import shutil
import xlwt
import var

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Event():

    def mensaje(title, text):
        """

        Muestra un mensaje informativo.

        :param title: Título del mensaje.
        :type title: str
        :param text: Texto del mensaje.
        :type text: str

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle(title)
        mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        mbox.setText(text)
        mbox.exec()



    def error(title, text):
        """

        Muestra un mensaje de error.

        :param title: Título del mensaje.
        :type title: str
        :param text: Texto del mensaje.
        :type text: str

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle(title)
        mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setText(text)
        mbox.exec()