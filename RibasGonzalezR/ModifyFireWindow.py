# Form implementation generated from reading ui file 'ModifyFireWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgModifyFireWindow(object):
    def setupUi(self, dlgModifyFireWindow):
        dlgModifyFireWindow.setObjectName("dlgModifyFireWindow")
        dlgModifyFireWindow.resize(400, 200)
        dlgModifyFireWindow.setMinimumSize(QtCore.QSize(400, 200))
        dlgModifyFireWindow.setMaximumSize(QtCore.QSize(400, 200))
        dlgModifyFireWindow.setStyleSheet("QHeaderView::section:horizontal {\n"
"    border-top: 1px solid #DEC09A;\n"
"    color: #FFF0CF;\n"
"    font: 11pt \"Arial\";\n"
"    background-color: #8294C4;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #8294C4;\n"
"    color: #FFFFFF; /* White text on dark background */\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color: #97A4C9;\n"
"    color: #FFFFFF; /* White text on dark background */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #000; /* Black text on light background */\n"
"    background-color: #97A4C9;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-color: #F9F0EF;\n"
"    background-color: #DBDFEA;\n"
"    color: #000000; /* Black text on light background */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 5px;\n"
"    background-color: #DCC5A0;\n"
"    color: #000000; /* Black text on light background */\n"
"}")
        self.lblModifyFireDate = QtWidgets.QLabel(parent=dlgModifyFireWindow)
        self.lblModifyFireDate.setGeometry(QtCore.QRect(60, 40, 281, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblModifyFireDate.sizePolicy().hasHeightForWidth())
        self.lblModifyFireDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblModifyFireDate.setFont(font)
        self.lblModifyFireDate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lblModifyFireDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblModifyFireDate.setObjectName("lblModifyFireDate")
        self.btnModifyFireDateYes = QtWidgets.QPushButton(parent=dlgModifyFireWindow)
        self.btnModifyFireDateYes.setGeometry(QtCore.QRect(90, 100, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifyFireDateYes.sizePolicy().hasHeightForWidth())
        self.btnModifyFireDateYes.setSizePolicy(sizePolicy)
        self.btnModifyFireDateYes.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnModifyFireDateYes.setObjectName("btnModifyFireDateYes")
        self.btnModifyFireDateNo = QtWidgets.QPushButton(parent=dlgModifyFireWindow)
        self.btnModifyFireDateNo.setGeometry(QtCore.QRect(220, 100, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifyFireDateNo.sizePolicy().hasHeightForWidth())
        self.btnModifyFireDateNo.setSizePolicy(sizePolicy)
        self.btnModifyFireDateNo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnModifyFireDateNo.setObjectName("btnModifyFireDateNo")

        self.retranslateUi(dlgModifyFireWindow)
        QtCore.QMetaObject.connectSlotsByName(dlgModifyFireWindow)

    def retranslateUi(self, dlgModifyFireWindow):
        _translate = QtCore.QCoreApplication.translate
        dlgModifyFireWindow.setWindowTitle(_translate("dlgModifyFireWindow", "Dialog"))
        self.lblModifyFireDate.setText(_translate("dlgModifyFireWindow", "DO YOU WANT TO CHANGE THE FIRE DATE?"))
        self.btnModifyFireDateYes.setText(_translate("dlgModifyFireWindow", "YES"))
        self.btnModifyFireDateNo.setText(_translate("dlgModifyFireWindow", "NO"))
