# Form implementation generated from reading ui file '.\templates\dlgSalir.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgSalir(object):
    def setupUi(self, dlgSalir):
        dlgSalir.setObjectName("dlgSalir")
        dlgSalir.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgSalir.resize(400, 300)
        dlgSalir.setMinimumSize(QtCore.QSize(400, 300))
        dlgSalir.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgSalir.setWindowIcon(icon)
        dlgSalir.setModal(True)
        self.frame = QtWidgets.QFrame(parent=dlgSalir)
        self.frame.setGeometry(QtCore.QRect(40, 20, 321, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 206, 215))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLogo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblLogo.setMinimumSize(QtCore.QSize(120, 120))
        self.lblLogo.setMaximumSize(QtCore.QSize(120, 120))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(".\\templates\\../img/salir.png"))
        self.lblLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.verticalLayout.addWidget(self.lblLogo, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lblSalir = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblSalir.setMinimumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblSalir.setFont(font)
        self.lblSalir.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSalir.setObjectName("lblSalir")
        self.verticalLayout.addWidget(self.lblSalir)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(23)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.btnSalir, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.btnCancelar = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout.addWidget(self.btnCancelar, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(dlgSalir)
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Salir"))
        self.lblSalir.setText(_translate("dlgSalir", "Desea Salir ?"))
        self.btnSalir.setText(_translate("dlgSalir", "Salir"))
        self.btnCancelar.setText(_translate("dlgSalir", "Cancelar"))
