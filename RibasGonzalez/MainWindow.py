# Form implementation generated from reading ui file './templates/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 777)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 777))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.panelPrincipal = QtWidgets.QTabWidget(parent=self.gridFrame)
        self.panelPrincipal.setMinimumSize(QtCore.QSize(900, 650))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.panelPrincipal.setFont(font)
        self.panelPrincipal.setObjectName("panelPrincipal")
        self.panelDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelDrivers.sizePolicy().hasHeightForWidth())
        self.panelDrivers.setSizePolicy(sizePolicy)
        self.panelDrivers.setAutoFillBackground(True)
        self.panelDrivers.setObjectName("panelDrivers")
        self.frngestdrive = QtWidgets.QFrame(parent=self.panelDrivers)
        self.frngestdrive.setGeometry(QtCore.QRect(9, 20, 961, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frngestdrive.sizePolicy().hasHeightForWidth())
        self.frngestdrive.setSizePolicy(sizePolicy)
        self.frngestdrive.setMinimumSize(QtCore.QSize(800, 80))
        self.frngestdrive.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frngestdrive.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frngestdrive.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frngestdrive.setObjectName("frngestdrive")
        self.lblNome = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblNome.setGeometry(QtCore.QRect(540, 50, 60, 20))
        self.lblNome.setMinimumSize(QtCore.QSize(60, 20))
        self.lblNome.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblNome.setObjectName("lblNome")
        self.lblValidardni = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblValidardni.setGeometry(QtCore.QRect(423, 11, 60, 30))
        self.lblValidardni.setMinimumSize(QtCore.QSize(60, 30))
        self.lblValidardni.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.lblValidardni.setFont(font)
        self.lblValidardni.setText("")
        self.lblValidardni.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblValidardni.setObjectName("lblValidardni")
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnCalendar.setGeometry(QtCore.QRect(920, 10, 28, 28))
        self.btnCalendar.setMinimumSize(QtCore.QSize(28, 28))
        self.btnCalendar.setMaximumSize(QtCore.QSize(28, 28))
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./templates\\../img/calendar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(28, 28))
        self.btnCalendar.setObjectName("btnCalendar")
        self.txtApel = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtApel.setGeometry(QtCore.QRect(86, 50, 350, 20))
        self.txtApel.setMinimumSize(QtCore.QSize(350, 20))
        self.txtApel.setMaximumSize(QtCore.QSize(350, 20))
        self.txtApel.setCursorPosition(0)
        self.txtApel.setObjectName("txtApel")
        self.lblApel = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblApel.setGeometry(QtCore.QRect(11, 50, 70, 20))
        self.lblApel.setMinimumSize(QtCore.QSize(70, 20))
        self.lblApel.setMaximumSize(QtCore.QSize(70, 20))
        self.lblApel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblApel.setObjectName("lblApel")
        self.lblcodbd = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblcodbd.setGeometry(QtCore.QRect(90, 10, 80, 20))
        self.lblcodbd.setMinimumSize(QtCore.QSize(80, 20))
        self.lblcodbd.setMaximumSize(QtCore.QSize(80, 20))
        self.lblcodbd.setStyleSheet("background-color: rgb(255, 248, 192);")
        self.lblcodbd.setText("")
        self.lblcodbd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcodbd.setObjectName("lblcodbd")
        self.txtDatadriver = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtDatadriver.setGeometry(QtCore.QRect(830, 20, 80, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDatadriver.sizePolicy().hasHeightForWidth())
        self.txtDatadriver.setSizePolicy(sizePolicy)
        self.txtDatadriver.setMinimumSize(QtCore.QSize(80, 20))
        self.txtDatadriver.setMaximumSize(QtCore.QSize(60, 20))
        self.txtDatadriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDatadriver.setObjectName("txtDatadriver")
        self.lblDni = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDni.setGeometry(QtCore.QRect(280, 10, 30, 20))
        self.lblDni.setMinimumSize(QtCore.QSize(30, 20))
        self.lblDni.setMaximumSize(QtCore.QSize(30, 20))
        self.lblDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDni.setObjectName("lblDni")
        self.txtDni = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtDni.setGeometry(QtCore.QRect(320, 10, 120, 20))
        self.txtDni.setMinimumSize(QtCore.QSize(120, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(120, 20))
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.lblCod = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblCod.setGeometry(QtCore.QRect(30, 10, 50, 20))
        self.lblCod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCod.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblCod.setObjectName("lblCod")
        self.lblDatadriver = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDatadriver.setGeometry(QtCore.QRect(710, 20, 110, 20))
        self.lblDatadriver.setMinimumSize(QtCore.QSize(110, 20))
        self.lblDatadriver.setMaximumSize(QtCore.QSize(110, 20))
        self.lblDatadriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDatadriver.setObjectName("lblDatadriver")
        self.txtNome = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtNome.setGeometry(QtCore.QRect(610, 50, 341, 20))
        self.txtNome.setMinimumSize(QtCore.QSize(300, 20))
        self.txtNome.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtNome.setObjectName("txtNome")
        self.lblDirdriver = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDirdriver.setGeometry(QtCore.QRect(10, 100, 70, 16))
        self.lblDirdriver.setMaximumSize(QtCore.QSize(70, 20))
        self.lblDirdriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDirdriver.setObjectName("lblDirdriver")
        self.txtDirdriver = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtDirdriver.setGeometry(QtCore.QRect(89, 100, 350, 20))
        self.txtDirdriver.setMinimumSize(QtCore.QSize(350, 20))
        self.txtDirdriver.setMaximumSize(QtCore.QSize(350, 20))
        self.txtDirdriver.setObjectName("txtDirdriver")
        self.lblMovil = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblMovil.setGeometry(QtCore.QRect(20, 140, 61, 20))
        self.lblMovil.setMaximumSize(QtCore.QSize(70, 20))
        self.lblMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblMovil.setObjectName("lblMovil")
        self.cmbMuni = QtWidgets.QComboBox(parent=self.frngestdrive)
        self.cmbMuni.setGeometry(QtCore.QRect(770, 100, 180, 20))
        self.cmbMuni.setMinimumSize(QtCore.QSize(180, 20))
        self.cmbMuni.setMaximumSize(QtCore.QSize(180, 20))
        self.cmbMuni.setObjectName("cmbMuni")
        self.lblPRov = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblPRov.setGeometry(QtCore.QRect(450, 100, 70, 20))
        self.lblPRov.setMaximumSize(QtCore.QSize(70, 20))
        self.lblPRov.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblPRov.setObjectName("lblPRov")
        self.cmbProv = QtWidgets.QComboBox(parent=self.frngestdrive)
        self.cmbProv.setGeometry(QtCore.QRect(530, 100, 150, 20))
        self.cmbProv.setMinimumSize(QtCore.QSize(150, 20))
        self.cmbProv.setMaximumSize(QtCore.QSize(150, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblLocalidad.setGeometry(QtCore.QRect(690, 100, 70, 16))
        self.lblLocalidad.setMaximumSize(QtCore.QSize(70, 20))
        self.lblLocalidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.txtMovil = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtMovil.setGeometry(QtCore.QRect(90, 140, 120, 20))
        self.txtMovil.setMinimumSize(QtCore.QSize(120, 20))
        self.txtMovil.setMaximumSize(QtCore.QSize(120, 20))
        self.txtMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtMovil.setObjectName("txtMovil")
        self.lblMovil_2 = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblMovil_2.setGeometry(QtCore.QRect(250, 140, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lblMovil_2.sizePolicy().hasHeightForWidth())
        self.lblMovil_2.setSizePolicy(sizePolicy)
        self.lblMovil_2.setMinimumSize(QtCore.QSize(60, 20))
        self.lblMovil_2.setMaximumSize(QtCore.QSize(60, 20))
        self.lblMovil_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblMovil_2.setObjectName("lblMovil_2")
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtSalario.setGeometry(QtCore.QRect(320, 140, 120, 20))
        self.txtSalario.setMinimumSize(QtCore.QSize(120, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(120, 20))
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtSalario.setObjectName("txtSalario")
        self.lblCarnet = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblCarnet.setGeometry(QtCore.QRect(30, 180, 100, 20))
        self.lblCarnet.setMinimumSize(QtCore.QSize(80, 0))
        self.lblCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblCarnet.setObjectName("lblCarnet")
        self.chkA = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkA.setGeometry(QtCore.QRect(150, 180, 41, 17))
        self.chkA.setObjectName("chkA")
        self.chkB = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkB.setGeometry(QtCore.QRect(200, 180, 41, 17))
        self.chkB.setObjectName("chkB")
        self.chkC = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkC.setGeometry(QtCore.QRect(250, 180, 41, 17))
        self.chkC.setObjectName("chkC")
        self.chkD = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkD.setGeometry(QtCore.QRect(300, 180, 41, 17))
        self.chkD.setObjectName("chkD")
        self.lblEstado = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblEstado.setGeometry(QtCore.QRect(610, 140, 80, 20))
        self.lblEstado.setMinimumSize(QtCore.QSize(80, 0))
        self.lblEstado.setMaximumSize(QtCore.QSize(100, 20))
        self.lblEstado.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblEstado.setObjectName("lblEstado")
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtAlta.setGeometry(QtCore.QRect(790, 140, 61, 17))
        self.rbtAlta.setObjectName("rbtAlta")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtAlta)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtBaja.setGeometry(QtCore.QRect(880, 140, 61, 17))
        self.rbtBaja.setObjectName("rbtBaja")
        self.buttonGroup.addButton(self.rbtBaja)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtTodos.setGeometry(QtCore.QRect(710, 140, 61, 17))
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.buttonGroup.addButton(self.rbtTodos)
        self.layoutWidget = QtWidgets.QWidget(parent=self.frngestdrive)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 220, 341, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_2.addWidget(self.btnAltaDriver)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_2.addWidget(self.btnModifDriver)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_2.addWidget(self.btnBajaDriver)
        self.splitter = QtWidgets.QSplitter(parent=self.panelDrivers)
        self.splitter.setGeometry(QtCore.QRect(0, 80, 80, 20))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabDrivers = QtWidgets.QTableWidget(parent=self.panelDrivers)
        self.tabDrivers.setGeometry(QtCore.QRect(10, 290, 961, 321))
        self.tabDrivers.setStyleSheet("QHeaderView::section:horizontal\n"
"{\n"
"border-top: 1px solid #ffffff;\n"
"color:\'white\';\n"
"font: 11pt \"Arial\";\n"
"background-color:rgb(100,100,100);\n"
"}")
        self.tabDrivers.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setObjectName("tabDrivers")
        self.tabDrivers.setColumnCount(6)
        self.tabDrivers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(5, item)
        self.tabDrivers.verticalHeader().setVisible(False)
        self.panelPrincipal.addTab(self.panelDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 131, 16))
        self.label_2.setObjectName("label_2")
        self.panelPrincipal.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.panelPrincipal, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionbarSalir = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./templates\\../img/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionbarSalir.setIcon(icon2)
        self.actionbarSalir.setObjectName("actionbarSalir")
        self.actionlimpiaPaneldriver = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./templates\\../img/limpiar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionlimpiaPaneldriver.setIcon(icon3)
        self.actionlimpiaPaneldriver.setObjectName("actionlimpiaPaneldriver")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionlimpiaPaneldriver)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbarSalir)

        self.retranslateUi(MainWindow)
        self.panelPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.panelPrincipal, self.txtDni)
        MainWindow.setTabOrder(self.txtDni, self.txtDatadriver)
        MainWindow.setTabOrder(self.txtDatadriver, self.btnCalendar)
        MainWindow.setTabOrder(self.btnCalendar, self.txtApel)
        MainWindow.setTabOrder(self.txtApel, self.txtNome)
        MainWindow.setTabOrder(self.txtNome, self.txtDirdriver)
        MainWindow.setTabOrder(self.txtDirdriver, self.cmbProv)
        MainWindow.setTabOrder(self.cmbProv, self.cmbMuni)
        MainWindow.setTabOrder(self.cmbMuni, self.txtMovil)
        MainWindow.setTabOrder(self.txtMovil, self.txtSalario)
        MainWindow.setTabOrder(self.txtSalario, self.chkA)
        MainWindow.setTabOrder(self.chkA, self.chkB)
        MainWindow.setTabOrder(self.chkB, self.chkC)
        MainWindow.setTabOrder(self.chkC, self.chkD)
        MainWindow.setTabOrder(self.chkD, self.btnAltaDriver)
        MainWindow.setTabOrder(self.btnAltaDriver, self.btnModifDriver)
        MainWindow.setTabOrder(self.btnModifDriver, self.btnBajaDriver)
        MainWindow.setTabOrder(self.btnBajaDriver, self.rbtTodos)
        MainWindow.setTabOrder(self.rbtTodos, self.rbtAlta)
        MainWindow.setTabOrder(self.rbtAlta, self.rbtBaja)
        MainWindow.setTabOrder(self.rbtBaja, self.tabDrivers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblDni.setText(_translate("MainWindow", "DNI:"))
        self.txtDni.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Introducir DNI</span></p></body></html>"))
        self.lblCod.setText(_translate("MainWindow", "Código:"))
        self.lblDatadriver.setText(_translate("MainWindow", "Fecha Alta:"))
        self.lblDirdriver.setText(_translate("MainWindow", "Dirección:"))
        self.lblMovil.setText(_translate("MainWindow", "Móvil:"))
        self.lblPRov.setText(_translate("MainWindow", "Provincia:"))
        self.lblLocalidad.setText(_translate("MainWindow", "Localidad:"))
        self.lblMovil_2.setText(_translate("MainWindow", "Salario:"))
        self.lblCarnet.setText(_translate("MainWindow", "Tipo de Carnet:"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.lblEstado.setText(_translate("MainWindow", "Histórico:"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.btnAltaDriver.setText(_translate("MainWindow", "Alta"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabDrivers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Móvil"))
        item = self.tabDrivers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Licencias"))
        item = self.tabDrivers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Baja"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.panelDrivers), _translate("MainWindow", "CONDUCTORES"))
        self.label_2.setText(_translate("MainWindow", "Esta es la pestaña 2"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))
        self.actionbarSalir.setText(_translate("MainWindow", "barSalir"))
        self.actionlimpiaPaneldriver.setText(_translate("MainWindow", "limpiaPaneldriver"))
