# Form implementation generated from reading ui file './templates/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 800))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1100, 730))
        self.tabWidget.setMinimumSize(QtCore.QSize(1100, 730))
        self.tabWidget.setMaximumSize(QtCore.QSize(1100, 730))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 1070, 40))
        self.frame_2.setMinimumSize(QtCore.QSize(1070, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(1070, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lblCategory = QtWidgets.QLabel(parent=self.frame_2)
        self.lblCategory.setGeometry(QtCore.QRect(30, 12, 70, 20))
        self.lblCategory.setMinimumSize(QtCore.QSize(70, 20))
        self.lblCategory.setMaximumSize(QtCore.QSize(70, 20))
        self.lblCategory.setObjectName("lblCategory")
        self.rbtIndividual = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rbtIndividual.setGeometry(QtCore.QRect(200, 12, 300, 20))
        self.rbtIndividual.setMinimumSize(QtCore.QSize(300, 20))
        self.rbtIndividual.setMaximumSize(QtCore.QSize(300, 20))
        self.rbtIndividual.setChecked(True)
        self.rbtIndividual.setObjectName("rbtIndividual")
        self.rbtBusiness = QtWidgets.QRadioButton(parent=self.frame_2)
        self.rbtBusiness.setGeometry(QtCore.QRect(700, 12, 300, 20))
        self.rbtBusiness.setMinimumSize(QtCore.QSize(300, 20))
        self.rbtBusiness.setMaximumSize(QtCore.QSize(300, 20))
        self.rbtBusiness.setObjectName("rbtBusiness")
        self.frame = QtWidgets.QFrame(parent=self.tab_3)
        self.frame.setGeometry(QtCore.QRect(10, 70, 450, 620))
        self.frame.setMinimumSize(QtCore.QSize(450, 620))
        self.frame.setMaximumSize(QtCore.QSize(450, 620))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #ACB1D6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: #97A4C9;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblIdCustomer = QtWidgets.QLabel(parent=self.frame)
        self.lblIdCustomer.setGeometry(QtCore.QRect(40, 20, 70, 25))
        self.lblIdCustomer.setMinimumSize(QtCore.QSize(70, 25))
        self.lblIdCustomer.setMaximumSize(QtCore.QSize(70, 25))
        self.lblIdCustomer.setObjectName("lblIdCustomer")
        self.lblName = QtWidgets.QLabel(parent=self.frame)
        self.lblName.setGeometry(QtCore.QRect(40, 120, 70, 25))
        self.lblName.setMinimumSize(QtCore.QSize(70, 25))
        self.lblName.setMaximumSize(QtCore.QSize(70, 25))
        self.lblName.setObjectName("lblName")
        self.lblSurname = QtWidgets.QLabel(parent=self.frame)
        self.lblSurname.setGeometry(QtCore.QRect(40, 70, 70, 25))
        self.lblSurname.setMinimumSize(QtCore.QSize(70, 25))
        self.lblSurname.setMaximumSize(QtCore.QSize(70, 25))
        self.lblSurname.setObjectName("lblSurname")
        self.lblAddress = QtWidgets.QLabel(parent=self.frame)
        self.lblAddress.setGeometry(QtCore.QRect(40, 170, 70, 25))
        self.lblAddress.setMinimumSize(QtCore.QSize(70, 25))
        self.lblAddress.setMaximumSize(QtCore.QSize(70, 25))
        self.lblAddress.setObjectName("lblAddress")
        self.lblEnrollDate = QtWidgets.QLabel(parent=self.frame)
        self.lblEnrollDate.setGeometry(QtCore.QRect(40, 270, 80, 25))
        self.lblEnrollDate.setMinimumSize(QtCore.QSize(80, 25))
        self.lblEnrollDate.setMaximumSize(QtCore.QSize(80, 25))
        self.lblEnrollDate.setObjectName("lblEnrollDate")
        self.lblTelephone = QtWidgets.QLabel(parent=self.frame)
        self.lblTelephone.setGeometry(QtCore.QRect(40, 320, 70, 25))
        self.lblTelephone.setMinimumSize(QtCore.QSize(70, 25))
        self.lblTelephone.setMaximumSize(QtCore.QSize(70, 25))
        self.lblTelephone.setObjectName("lblTelephone")
        self.lblEmail = QtWidgets.QLabel(parent=self.frame)
        self.lblEmail.setGeometry(QtCore.QRect(40, 220, 70, 25))
        self.lblEmail.setMinimumSize(QtCore.QSize(70, 25))
        self.lblEmail.setMaximumSize(QtCore.QSize(70, 25))
        self.lblEmail.setObjectName("lblEmail")
        self.lblId = QtWidgets.QLabel(parent=self.frame)
        self.lblId.setGeometry(QtCore.QRect(130, 20, 120, 25))
        self.lblId.setMinimumSize(QtCore.QSize(120, 25))
        self.lblId.setMaximumSize(QtCore.QSize(120, 25))
        self.lblId.setStyleSheet("background:  rgb(255, 254, 196)")
        self.lblId.setText("")
        self.lblId.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblId.setObjectName("lblId")
        self.txtName = QtWidgets.QLineEdit(parent=self.frame)
        self.txtName.setGeometry(QtCore.QRect(130, 120, 200, 25))
        self.txtName.setMinimumSize(QtCore.QSize(200, 25))
        self.txtName.setMaximumSize(QtCore.QSize(200, 25))
        self.txtName.setObjectName("txtName")
        self.txtSurname = QtWidgets.QLineEdit(parent=self.frame)
        self.txtSurname.setGeometry(QtCore.QRect(130, 70, 300, 25))
        self.txtSurname.setMinimumSize(QtCore.QSize(300, 25))
        self.txtSurname.setMaximumSize(QtCore.QSize(300, 25))
        self.txtSurname.setObjectName("txtSurname")
        self.txtAddress = QtWidgets.QLineEdit(parent=self.frame)
        self.txtAddress.setGeometry(QtCore.QRect(130, 170, 300, 25))
        self.txtAddress.setMinimumSize(QtCore.QSize(300, 25))
        self.txtAddress.setMaximumSize(QtCore.QSize(300, 25))
        self.txtAddress.setObjectName("txtAddress")
        self.txtTelephone = QtWidgets.QLineEdit(parent=self.frame)
        self.txtTelephone.setGeometry(QtCore.QRect(130, 320, 150, 25))
        self.txtTelephone.setMinimumSize(QtCore.QSize(150, 25))
        self.txtTelephone.setMaximumSize(QtCore.QSize(150, 25))
        self.txtTelephone.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtTelephone.setObjectName("txtTelephone")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.frame)
        self.txtEmail.setGeometry(QtCore.QRect(130, 220, 300, 25))
        self.txtEmail.setMinimumSize(QtCore.QSize(300, 25))
        self.txtEmail.setMaximumSize(QtCore.QSize(300, 25))
        self.txtEmail.setObjectName("txtEmail")
        self.txtEnrollDate = QtWidgets.QLineEdit(parent=self.frame)
        self.txtEnrollDate.setGeometry(QtCore.QRect(130, 270, 150, 25))
        self.txtEnrollDate.setMinimumSize(QtCore.QSize(150, 25))
        self.txtEnrollDate.setMaximumSize(QtCore.QSize(150, 25))
        self.txtEnrollDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtEnrollDate.setObjectName("txtEnrollDate")
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendar.setGeometry(QtCore.QRect(280, 270, 30, 25))
        self.btnCalendar.setMinimumSize(QtCore.QSize(30, 25))
        self.btnCalendar.setMaximumSize(QtCore.QSize(30, 25))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./templates\\../images/calendario.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(24, 24))
        self.btnCalendar.setObjectName("btnCalendar")
        self.btnEnroll = QtWidgets.QPushButton(parent=self.frame)
        self.btnEnroll.setGeometry(QtCore.QRect(170, 400, 100, 25))
        self.btnEnroll.setMinimumSize(QtCore.QSize(100, 25))
        self.btnEnroll.setMaximumSize(QtCore.QSize(100, 25))
        self.btnEnroll.setObjectName("btnEnroll")
        self.btnModify = QtWidgets.QPushButton(parent=self.frame)
        self.btnModify.setGeometry(QtCore.QRect(170, 450, 100, 25))
        self.btnModify.setMinimumSize(QtCore.QSize(100, 25))
        self.btnModify.setMaximumSize(QtCore.QSize(100, 25))
        self.btnModify.setObjectName("btnModify")
        self.btnFire = QtWidgets.QPushButton(parent=self.frame)
        self.btnFire.setGeometry(QtCore.QRect(170, 500, 100, 25))
        self.btnFire.setMinimumSize(QtCore.QSize(100, 25))
        self.btnFire.setMaximumSize(QtCore.QSize(100, 25))
        self.btnFire.setObjectName("btnFire")
        self.frame_3 = QtWidgets.QFrame(parent=self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(470, 70, 610, 40))
        self.frame_3.setMinimumSize(QtCore.QSize(610, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(610, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lblHistorical = QtWidgets.QLabel(parent=self.frame_3)
        self.lblHistorical.setGeometry(QtCore.QRect(20, 10, 70, 25))
        self.lblHistorical.setMinimumSize(QtCore.QSize(70, 25))
        self.lblHistorical.setMaximumSize(QtCore.QSize(70, 25))
        self.lblHistorical.setObjectName("lblHistorical")
        self.chkAll = QtWidgets.QCheckBox(parent=self.frame_3)
        self.chkAll.setGeometry(QtCore.QRect(100, 10, 300, 25))
        self.chkAll.setMinimumSize(QtCore.QSize(300, 25))
        self.chkAll.setMaximumSize(QtCore.QSize(300, 25))
        self.chkAll.setObjectName("chkAll")
        self.tabCustomers = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tabCustomers.setGeometry(QtCore.QRect(470, 130, 610, 560))
        self.tabCustomers.setMinimumSize(QtCore.QSize(610, 560))
        self.tabCustomers.setMaximumSize(QtCore.QSize(610, 560))
        self.tabCustomers.setStyleSheet("QTableWidget::item:selected {\n"
"    background-color:  : #C59A6C;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #ACB1D6;\n"
"}")
        self.tabCustomers.setObjectName("tabCustomers")
        self.tabCustomers.setColumnCount(5)
        self.tabCustomers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabCustomers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCustomers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCustomers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCustomers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabCustomers.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabProducts = QtWidgets.QTableWidget(parent=self.tab_4)
        self.tabProducts.setGeometry(QtCore.QRect(40, 250, 1025, 440))
        self.tabProducts.setMinimumSize(QtCore.QSize(1025, 440))
        self.tabProducts.setMaximumSize(QtCore.QSize(1025, 440))
        self.tabProducts.setStyleSheet("QTableWidget::item:selected {\n"
"    background-color:  : #C59A6C;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #ACB1D6;\n"
"}")
        self.tabProducts.setObjectName("tabProducts")
        self.tabProducts.setColumnCount(4)
        self.tabProducts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabProducts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabProducts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabProducts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabProducts.setHorizontalHeaderItem(3, item)
        self.frame_4 = QtWidgets.QFrame(parent=self.tab_4)
        self.frame_4.setGeometry(QtCore.QRect(40, 20, 1025, 200))
        self.frame_4.setMinimumSize(QtCore.QSize(1025, 200))
        self.frame_4.setMaximumSize(QtCore.QSize(1025, 200))
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: #ACB1D6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox{\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: #97A4C9;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lblNamePro = QtWidgets.QLabel(parent=self.frame_4)
        self.lblNamePro.setGeometry(QtCore.QRect(40, 90, 70, 25))
        self.lblNamePro.setMinimumSize(QtCore.QSize(70, 25))
        self.lblNamePro.setMaximumSize(QtCore.QSize(70, 25))
        self.lblNamePro.setObjectName("lblNamePro")
        self.txtNamePro = QtWidgets.QLineEdit(parent=self.frame_4)
        self.txtNamePro.setGeometry(QtCore.QRect(140, 90, 200, 25))
        self.txtNamePro.setMinimumSize(QtCore.QSize(200, 25))
        self.txtNamePro.setMaximumSize(QtCore.QSize(200, 25))
        self.txtNamePro.setObjectName("txtNamePro")
        self.btnAdd = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnAdd.setGeometry(QtCore.QRect(190, 150, 100, 25))
        self.btnAdd.setMinimumSize(QtCore.QSize(100, 25))
        self.btnAdd.setMaximumSize(QtCore.QSize(100, 25))
        self.btnAdd.setObjectName("btnAdd")
        self.btnModify_2 = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnModify_2.setGeometry(QtCore.QRect(450, 150, 100, 25))
        self.btnModify_2.setMinimumSize(QtCore.QSize(100, 25))
        self.btnModify_2.setMaximumSize(QtCore.QSize(100, 25))
        self.btnModify_2.setObjectName("btnModify_2")
        self.btnRemove = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnRemove.setGeometry(QtCore.QRect(700, 150, 100, 25))
        self.btnRemove.setMinimumSize(QtCore.QSize(100, 25))
        self.btnRemove.setMaximumSize(QtCore.QSize(100, 25))
        self.btnRemove.setObjectName("btnRemove")
        self.lblIdProduct = QtWidgets.QLabel(parent=self.frame_4)
        self.lblIdProduct.setGeometry(QtCore.QRect(40, 30, 70, 25))
        self.lblIdProduct.setMinimumSize(QtCore.QSize(70, 25))
        self.lblIdProduct.setMaximumSize(QtCore.QSize(70, 25))
        self.lblIdProduct.setObjectName("lblIdProduct")
        self.lblIdPro = QtWidgets.QLabel(parent=self.frame_4)
        self.lblIdPro.setGeometry(QtCore.QRect(140, 30, 120, 25))
        self.lblIdPro.setMinimumSize(QtCore.QSize(120, 25))
        self.lblIdPro.setMaximumSize(QtCore.QSize(120, 25))
        self.lblIdPro.setStyleSheet("background:  rgb(255, 254, 196)")
        self.lblIdPro.setText("")
        self.lblIdPro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblIdPro.setObjectName("lblIdPro")
        self.lblPricePro = QtWidgets.QLabel(parent=self.frame_4)
        self.lblPricePro.setGeometry(QtCore.QRect(390, 90, 70, 25))
        self.lblPricePro.setMinimumSize(QtCore.QSize(70, 25))
        self.lblPricePro.setMaximumSize(QtCore.QSize(70, 25))
        self.lblPricePro.setObjectName("lblPricePro")
        self.spStockPro = QtWidgets.QSpinBox(parent=self.frame_4)
        self.spStockPro.setGeometry(QtCore.QRect(800, 90, 75, 25))
        self.spStockPro.setMinimumSize(QtCore.QSize(75, 25))
        self.spStockPro.setMaximumSize(QtCore.QSize(75, 25))
        self.spStockPro.setObjectName("spStockPro")
        self.txtPricePro = QtWidgets.QLineEdit(parent=self.frame_4)
        self.txtPricePro.setGeometry(QtCore.QRect(500, 90, 150, 25))
        self.txtPricePro.setMinimumSize(QtCore.QSize(150, 25))
        self.txtPricePro.setMaximumSize(QtCore.QSize(150, 25))
        self.txtPricePro.setObjectName("txtPricePro")
        self.lblStockPro = QtWidgets.QLabel(parent=self.frame_4)
        self.lblStockPro.setGeometry(QtCore.QRect(700, 90, 70, 25))
        self.lblStockPro.setMinimumSize(QtCore.QSize(70, 25))
        self.lblStockPro.setMaximumSize(QtCore.QSize(70, 25))
        self.lblStockPro.setObjectName("lblStockPro")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menuCustomers = QtWidgets.QMenu(parent=self.menubar)
        self.menuCustomers.setObjectName("menuCustomers")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuInformes = QtWidgets.QMenu(parent=self.menubar)
        self.menuInformes.setObjectName("menuInformes")
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionCreate_Customers_Report_PDF = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./templates\\../images/crearreport.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_Customers_Report_PDF.setIcon(icon1)
        self.actionCreate_Customers_Report_PDF.setObjectName("actionCreate_Customers_Report_PDF")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./templates\\../images/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionclearWindow = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./templates\\../images/actualizar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionclearWindow.setIcon(icon3)
        self.actionclearWindow.setObjectName("actionclearWindow")
        self.menuCustomers.addAction(self.actionExit)
        self.menuInformes.addAction(self.actionCreate_Customers_Report_PDF)
        self.menubar.addAction(self.menuCustomers.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionCreate_Customers_Report_PDF)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionclearWindow)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LibreriaTeis"))
        self.lblCategory.setText(_translate("MainWindow", "Category:"))
        self.rbtIndividual.setText(_translate("MainWindow", "Individual"))
        self.rbtBusiness.setText(_translate("MainWindow", "Business"))
        self.lblIdCustomer.setText(_translate("MainWindow", "Id:"))
        self.lblName.setText(_translate("MainWindow", "Name:"))
        self.lblSurname.setText(_translate("MainWindow", "Surname:"))
        self.lblAddress.setText(_translate("MainWindow", "Address:"))
        self.lblEnrollDate.setText(_translate("MainWindow", "Enroll Date:"))
        self.lblTelephone.setText(_translate("MainWindow", "Telephone:"))
        self.lblEmail.setText(_translate("MainWindow", "Email:"))
        self.btnEnroll.setText(_translate("MainWindow", "Enroll"))
        self.btnModify.setText(_translate("MainWindow", "Modify"))
        self.btnFire.setText(_translate("MainWindow", "Fire"))
        self.lblHistorical.setText(_translate("MainWindow", "Historical:"))
        self.chkAll.setText(_translate("MainWindow", "Show All"))
        item = self.tabCustomers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tabCustomers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tabCustomers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tabCustomers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telephone"))
        item = self.tabCustomers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Customers"))
        item = self.tabProducts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tabProducts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tabProducts.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tabProducts.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        self.lblNamePro.setText(_translate("MainWindow", "Name:"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnModify_2.setText(_translate("MainWindow", "Modify"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.lblIdProduct.setText(_translate("MainWindow", "Id:"))
        self.lblPricePro.setText(_translate("MainWindow", "Price:"))
        self.lblStockPro.setText(_translate("MainWindow", "Stock:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Products"))
        self.menuCustomers.setTitle(_translate("MainWindow", "File"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Tools"))
        self.menuInformes.setTitle(_translate("MainWindow", "Reports"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCreate_Customers_Report_PDF.setText(_translate("MainWindow", "Create Customers Report PDF"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionclearWindow.setText(_translate("MainWindow", "clearWindow"))
        self.actionclearWindow.setToolTip(_translate("MainWindow", "clearWindow"))
