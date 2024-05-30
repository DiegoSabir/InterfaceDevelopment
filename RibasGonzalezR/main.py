import locale
import sys

import customers
import events
import invoices
import products
import reports
import var
import connection
import auxiliary

from MainWindow import *
from auxiliary import *

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.exitWindow = Exit()
        var.dlgModifyFireWindow = Fire()

        connection.Connection.connection()


        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(events.Events.openCalendar)
        var.ui.btnEnroll.clicked.connect(customers.Customers.enrollCustomer)
        var.ui.btnModify.clicked.connect(customers.Customers.modifyCustomer)
        var.ui.btnFire.clicked.connect(customers.Customers.fireCustomer)
        var.ui.btnAdd.clicked.connect(products.Products.addProduct)
        var.ui.btnModify_2.clicked.connect(products.Products.modifyProduct)
        var.ui.btnRemove.clicked.connect(products.Products.removeProduct)
        var.ui.cmbIdCustomer.currentIndexChanged.connect(connection.Connection.select_customer_id)
        var.ui.btnCalendarInvoice.clicked.connect(events.Events.open_calendar_invoice)


        '''
        Zona de eventos de check box
        '''
        var.ui.chkAll.stateChanged.connect(connection.Connection.showCustomers)


        '''
        Zona de eventos dos menubars
        '''



        '''
        Zona de cajas de texto
        '''
        var.ui.txtSurname.editingFinished.connect(events.Events.capitalLetter)
        var.ui.txtName.editingFinished.connect(events.Events.capitalLetter)
        var.ui.txtEmail.editingFinished.connect(events.Events.checkEmailFormat)
        var.ui.txtPricePro.editingFinished.connect(events.Events.checkPriceFormat)
        var.ui.rbtBusiness.clicked.connect(events.Events.blockTxtSurname)
        var.ui.rbtIndividual.clicked.connect(events.Events.unblockTxtSurname)


        '''
        Zona de eventos da toolbar
        '''
        var.ui.actionExit.triggered.connect(events.Events.showExit)
        var.ui.actionclearWindow.triggered.connect(customers.Customers.clear)
        var.ui.actionCreate_Customers_Report_PDF.triggered.connect(reports.Reports.reportCustomers)
        var.ui.actionCreate_Products_Report_PDF.triggered.connect(reports.Reports.reportProducts)


        '''
        Zona de init
        '''
        connection.Connection.showCustomers()
        connection.Connection.showProducts()
        connection.Connection.show_invoices()


        '''
        Eventos de Tablas
        '''
        events.Events.resizeCustomerTable()
        events.Events.resizeProductTable()
        events.Events.resize_invoice_tab()
        var.ui.tabCustomers.clicked.connect(customers.Customers.loadCustomers)
        var.ui.tabProducts.clicked.connect(products.Products.loadProducts)
        var.ui.tabInvoices.clicked.connect(invoices.Invoices.load_invoices)


    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox()
        mbox.setStyleSheet("QDialog{background-color: #8294C4;} "
                           "QLabel {color: rgb(0, 0, 0);} ")
        mbox.setWindowTitle("Exit")
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setText("¿Do you want to Exit?")

        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Yes')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        resultado = mbox.exec()

        if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
