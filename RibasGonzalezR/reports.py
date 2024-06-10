from datetime import datetime
from PIL import Image
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas

import os
import var


class Reports:
    @staticmethod
    def report_customers():
        """
        Genera un informe en PDF de la lista de clientes.

        :return: None
        """
        try:
            date = datetime.today()
            date = date.strftime('%Y_%m_%d_%H_%M_%S')
            name = date + '_customersList.pdf'
            var.report = canvas.Canvas('reports/' + name)
            title = 'Customers List'
            Reports.top_report(title)
            Reports.bot_report(title)
            items = ['ID', 'Name', 'Telephone', 'Address', 'Email']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))
            var.report.drawString(200, 675, str(items[2]))
            var.report.drawString(300, 675, str(items[3]))
            var.report.drawString(450, 675, str(items[4]))
            var.report.line(50, 670, 570, 670)

            query = QtSql.QSqlQuery()
            if var.ui.rbtIndividual.isChecked():
                if var.ui.chkAll.isChecked():
                    query.prepare('SELECT id_customer, name_customer, telephone_customer, address_customer,  email_customer, firedate_customer FROM customer WHERE category_customer IS "Individual"')

                else:
                    query.prepare('SELECT id_customer, name_customer, telephone_customer, address_customer, email_customer, firedate_customer FROM customer WHERE firedate_customer IS NULL AND category_customer IS "Individual"')

            elif var.ui.rbtBusiness.isChecked():
                if var.ui.chkAll.isChecked():
                    query.prepare('SELECT id_customer, name_customer, telephone_customer, address_customer, email_customer, firedate_customer FROM customer WHERE category_customer IS "Bussiness"')

                else:
                    query.prepare('SELECT id_customer, name_customer, telephone_customer, address_customer, email_customer, firedate_customer FROM customer WHERE firedate_customer IS NULL AND category_customer IS "Bussiness"')

            if query.exec():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.showPage()  # Crear una pagina nueva
                        Reports.top_report(title)
                        Reports.bot_report(title)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(100, 675, str(items[1]))
                        var.report.drawString(200, 675, str(items[2]))
                        var.report.drawString(300, 675, str(items[3]))
                        var.report.drawString(450, 675, str(items[4]))
                        var.report.line(50, 670, 570, 670)
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 150, j, str(query.value(2)))
                    var.report.drawString(i + 250, j, str(query.value(3)))
                    var.report.drawString(i + 400, j, str(query.value(4)))
                    j -= 25
            else:
                print("Query Error:", query.lastError().text())

            var.report.save()
            rootPath = '.\\reports'
            for file in os.listdir(rootPath):
                if file.endswith(name):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print("Error en report_customers from reports: ", error)



    @staticmethod
    def report_products():
        """
        Genera un informe en PDF de la lista de productos.

        :return: None
        """
        try:
            date = datetime.today()
            date = date.strftime('%Y_%m_%d_%H_%M_%S')
            name = date + '_productsList.pdf'
            var.report = canvas.Canvas('reports/' + name)
            title = 'Products List'
            Reports.top_report(title)
            Reports.bot_report(title)
            items = ['ID', 'Name', 'Price', 'Stock']  # Campos de la tabla de productos
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))  # Ajusta la coordenada x para el segundo título
            var.report.drawString(400, 675, str(items[2]))  # Ajusta la coordenada x para el tercer título
            var.report.drawString(500, 675, str(items[3]))  # Ajusta la coordenada x para el cuarto título
            var.report.line(50, 670, 570, 670)  # Ajusta la posición final de la línea de acuerdo a la cantidad de campos

            # Consulta SQL para obtener los productos
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_product, name_product, price_product, stock_product FROM product')
            if query.exec():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.showPage()  # Crear una página nueva
                        Reports.top_report(title)
                        Reports.bot_report(title)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(100, 675, str(items[1]))
                        var.report.drawString(400, 675, str(items[2]))
                        var.report.drawString(500, 675, str(items[3]))
                        var.report.line(50, 670, 570, 670)
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 350, j, str(query.value(2)))
                    var.report.drawString(i + 450, j, str(query.value(3)))
                    j -= 25
            else:
                print(query.lastError())

            var.report.save()
            rootPath = '.\\reports'
            for file in os.listdir(rootPath):
                if file.endswith(name):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print("error en report_products from reports: ", error)



    @staticmethod
    def report_invoices():
        """
        Genera un informe en PDF de la lista de facturas.

        :return: None
        """
        try:
            if var.ui.txtIdInvoiceSale.text() is str(""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Select an invoice")
                mbox.exec()

            else:
                # Generate file name
                fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
                nombre = f"{fecha}_invoiceList.pdf"
                var.report = canvas.Canvas(f'reports/{nombre}')
                title = 'Invoice List'

                Reports.top_report(title)
                Reports.bot_report(title)

                # Column titles
                items = ['IdSale', 'IdInvoice', 'Product', 'Quantity', 'Price', 'Total']
                var.report.setFont('Helvetica-Bold', size=10)
                var.report.drawString(50, 675, str(items[0]))
                var.report.drawString(100, 675, str(items[1]))
                var.report.drawString(200, 675, str(items[2]))
                var.report.drawString(410, 675, str(items[3]))
                var.report.drawString(480, 675, str(items[4]))
                var.report.drawString(540, 675, str(items[5]))
                var.report.line(50, 670, 570, 670)

                # Database query
                query = QtSql.QSqlQuery()
                query.prepare("SELECT sale.id_sale, sale.id_invoice_sale, product.name_product, sale.quantity_sale, sale.price_sale, (sale.quantity_sale * sale.price_sale) AS total FROM sale INNER JOIN product ON sale.id_product_sale = product.id_product WHERE id_invoice_sale = :dato")
                query.bindValue(":dato", var.ui.txtIdInvoice.text())  # You need to provide the value for :dato

                if query.exec():
                    i = 50
                    j = 655
                    while query.next():
                        if j <= 80:
                            var.report.showPage()  # Crear una pagina nueva
                            Reports.top_report(title)
                            Reports.bot_report(title)

                            var.report.drawString(50, 675, str(items[0]))
                            var.report.drawString(100, 675, str(items[1]))
                            var.report.drawString(200, 675, str(items[2]))
                            var.report.drawString(410, 675, str(items[3]))
                            var.report.drawString(480, 675, str(items[4]))
                            var.report.drawString(540, 675, str(items[5]))
                            var.report.line(50, 670, 570, 670)
                            j = 655
                        var.report.setFont('Helvetica', size=9)
                        var.report.drawString(i, j, str(query.value(0)))
                        var.report.drawString(i + 50, j, str(query.value(1)))
                        var.report.drawString(i + 150, j, str(query.value(2)))
                        var.report.drawString(i + 370, j, str(query.value(3)))
                        var.report.drawString(i + 430, j, str(query.value(4)))
                        var.report.drawString(i + 490, j, str(query.value(5)))
                        j -= 25
                else:
                    print(query.lastError().text())

                var.report.save()
                rootPath = '.\\reports'
                for file in os.listdir(rootPath):
                    if file.endswith(nombre):
                        os.startfile(os.path.join(rootPath, file))

        except Exception as error:
            print("error en report_invoices from reports: ", error)



    def top_report(title):
        """
        Configura la parte superior del informe PDF con el título y la información de la empresa.

        :param title: Título del informe.
        :return: None
        """
        try:
            ruta_logo = 'images/logo.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 570, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'LibreriaTeis')
                var.report.drawString(240, 695, title)
                var.report.line(50, 690, 570, 690)

                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - Spain')
                var.report.drawString(55, 725, 'Telephone: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: libreriateis@gmail.com')

            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')

        except Exception as error:
            print('error en top_report from reports:', error)



    def bot_report(title):
        """
        Configura la parte inferior del informe PDF con la fecha, el título y el número de página.

        :param title: Título del informe.
        :return: None
        """
        try:
            var.report.line(50, 50, 570, 50)
            date = datetime.today()
            date = date.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(date))
            var.report.drawString(250, 40, str(title))
            var.report.drawString(490, 40, str('Page %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en bot_report from reports: ', error)
