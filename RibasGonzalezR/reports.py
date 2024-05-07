from datetime import datetime
from PIL import Image
from PyQt6 import QtSql
from reportlab.pdfgen import canvas

import os
import var


class reports:
    @staticmethod
    def reportCustomers():
        try:
            date = datetime.today()
            date = date.strftime('%Y_%m_%d_%H_%M_%S')
            name = date + '_customersList.pdf'
            var.report = canvas.Canvas('reports/' + name)
            title = 'Customers List'
            reports.top_report(title)
            reports.bot_report(title)
            items = ['ID', 'Category', 'Name', 'Telephone', 'Address', 'Email']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))
            var.report.drawString(165, 675, str(items[2]))
            var.report.drawString(250, 675, str(items[3]))
            var.report.drawString(370, 675, str(items[4]))
            var.report.drawString(470, 675, str(items[5]))
            var.report.line(50, 670, 570, 670)

            query = QtSql.QSqlQuery()
            if var.ui.chkAll.isChecked():
                if var.ui.rbtBusiness.isChecked():
                    query.prepare('SELECT id_customer,category_customer,name_customer,telephone_customer,address_customer,email_customer from customer order by id_customer')
                elif var.ui.rbtIndividual.isChecked():
                    query.prepare('SELECT id_customer,category_customer,name_customer,telephone_customer,address_customer,email_customer from customer order by id_customer')

            else:
                if var.ui.rbtBusiness.isChecked():
                    query.prepare("SELECT id_customer,category_customer,name_customer,telephone_customer,address_customer,email_customer from customer WHERE category like 'Bussiness' order by id_customer")
                elif var.ui.rbtIndividual.isChecked():
                    query.prepare("SELECT id_customer,category_customer,name_customer,telephone_customer,address_customer,email_customer from customer WHERE category like 'Individual' order by id_customer")

            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 90, 'Next Page')
                        var.report.showPage()  # Crear una pagina nueva
                        reports.top_report(title)
                        reports.bot_report(title)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(100, 675, str(items[1]))
                        var.report.drawString(165, 675, str(items[2]))
                        var.report.drawString(280, 675, str(items[3]))
                        var.report.drawString(380, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 625, 570, 670)
                        i = 55
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 195, j, str(query.value(3)))
                    var.report.drawString(i + 320, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j = j-25
            else:
                print(query.lastError())

            var.report.save()
            rootPath='.\\reports'
            for file in os.listdir(rootPath):
                if file.endswith(name):
                    os.startfile('%s\\%s' % (rootPath,file))

        except Exception as error:
            print("error en reportCustomers from reports: ", error)



    def top_report(title):
        try:
            ruta_logo = 'images/logo.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
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
                var.report.drawString(55, 710, 'e-mail: LibreriaTeis@gmail.com')

            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')

        except Exception as error:
            print('error en top_report from reports:', error)



    def bot_report(title):
        try:
            var.report.line(50,50,570,50)
            date = datetime.today()
            date = date.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(date))
            var.report.drawString(250, 40, str(title))
            var.report.drawString(490, 40, str('Page %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en bot_report from reports: ', error)