# Form implementation generated from reading ui file '.\templates\acercaWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_acercaWind(object):
    def setupUi(self, acercaWind):
        acercaWind.setObjectName("acercaWind")
        acercaWind.resize(450, 310)
        acercaWind.setMinimumSize(QtCore.QSize(450, 310))
        acercaWind.setMaximumSize(QtCore.QSize(450, 310))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../img/Question-mark-icon_34771.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        acercaWind.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(parent=acercaWind)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(220, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(190, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\templates\\../img/icono.ico"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(140, 50, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 210, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btnaceptar = QtWidgets.QPushButton(parent=acercaWind)
        self.btnaceptar.setGeometry(QtCore.QRect(160, 270, 111, 31))
        self.btnaceptar.setObjectName("btnaceptar")

        self.retranslateUi(acercaWind)
        QtCore.QMetaObject.connectSlotsByName(acercaWind)

    def retranslateUi(self, acercaWind):
        _translate = QtCore.QCoreApplication.translate
        acercaWind.setWindowTitle(_translate("acercaWind", "Acerca de..."))
        self.label.setText(_translate("acercaWind", "CarTeis"))
        self.label_2.setText(_translate("acercaWind", "Version: 0.1.4.5"))
        self.label_4.setText(_translate("acercaWind", "Servicio privado de trasnporte perrsonal"))
        self.label_5.setText(_translate("acercaWind", "06/10/2023 - Jesús Blanco Miguez"))
        self.label_6.setText(_translate("acercaWind", "Proyecto de fin de curso"))
        self.label_7.setText(_translate("acercaWind", "Desarrollo de aplicaciones multiplataforma"))
        self.label_8.setText(_translate("acercaWind", "2023- IES de Teis"))
        self.btnaceptar.setText(_translate("acercaWind", "Aceptar"))
