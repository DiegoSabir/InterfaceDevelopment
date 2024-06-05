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
        var.calendarInvoice = CalendarInvoice()

        connection.Connection.connection()

        connection.Connection.load_customer()
        connection.Connection.load_product()
        connection.Connection.load_invoice()


        """
        Zona de eventos de botones
        """
        var.ui.btnCalendar.clicked.connect(events.Events.open_calendar)
        var.ui.btnEnroll.clicked.connect(customers.Customers.enroll_customer)
        var.ui.btnModify.clicked.connect(customers.Customers.modify_customer)
        var.ui.btnFire.clicked.connect(customers.Customers.fire_customer)
        var.ui.btnAdd.clicked.connect(products.Products.add_product)
        var.ui.btnModify_2.clicked.connect(products.Products.modify_product)
        var.ui.btnRemove.clicked.connect(products.Products.remove_product)
        var.ui.btnCalendarInvoice.clicked.connect(invoices.Invoices.open_calendar)
        var.ui.btnInvoice.clicked.connect(invoices.Invoices.enroll_invoice)
        var.ui.btnSaveSale.clicked.connect(invoices.Invoices.enroll_sale)
        var.ui.btnModifySale.clicked.connect(invoices.Invoices.modify_sale)


        '''
        Zona de eventos de check box
        '''
        var.ui.chkAll.stateChanged.connect(connection.Connection.show_customers)


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
        var.ui.actionExit.triggered.connect(events.Events.show_exit)
        var.ui.actionclearWindow.triggered.connect(events.Events.clear_all)
        var.ui.actionCreate_Customers_Report_PDF.triggered.connect(reports.Reports.report_customers)
        var.ui.actionCreate_Products_Report_PDF.triggered.connect(reports.Reports.report_products)


        '''
        Zona de init
        '''
        connection.Connection.show_customers()
        connection.Connection.show_products()



        '''
        Eventos de Tablas
        '''
        events.Events.resizeCustomerTable()
        events.Events.resizeProductTable()
        events.Events.resize_invoice_tab()
        events.Events.resize_sale_tab()

        var.ui.tabCustomers.clicked.connect(customers.Customers.load_customers)
        var.ui.tabProducts.clicked.connect(products.Products.load_products)
        var.ui.tabInvoices.clicked.connect(invoices.Invoices.load_invoice)
        var.ui.tabSale.clicked.connect(invoices.Invoices.load_sale)


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
