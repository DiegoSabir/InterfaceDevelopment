from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var
import re

class Customers:
    @staticmethod
    def validateEmail(email):
        try:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, email):
                var.ui.txtEmail.setText(email)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Invalid Email Format")
                mbox.exec()

        except Exception as error:
            print("error validating email ", error)



    @staticmethod
    def loadDate(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataDriver.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error loading data", error)



    @staticmethod
    def enrollCustomer():
        try:
            if var.ui.lblId.text() != "":
                codigo = var.ui.lblId.text()
                if Customers.checkFireDate(codigo):
                    connection.Connection.removeFireDate(codigo)
                    Customers.customerStatus()
            else:
                customer = [var.ui.txtSurname,
                            var.ui.txtName,
                            var.ui.txtBirthdate,
                            var.ui.txtAddress,
                            var.ui.txtTelephone,
                            var.ui.txtEmail]
                newcustomer = []
                for i in customer:
                    newcustomer.append(i.text().title())

                connection.Connection.saveCustomer(newcustomer)

        except Exception as error:
            print("Error with enroll customer", error)



    @staticmethod
    def checkFireDate(codigo):
        try:
            baja = True
            query = QtSql.QSqlQuery()
            query.prepare("select bajadri from drivers where codigo = :codigo")
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    fecha = query.value(0)
                    if fecha == "":
                        baja = False
            return baja

        except Exception as error:
            print('error when checking the fire date', error)



    @staticmethod
    def customerStatus():
        if var.ui.rbtAll.isChecked():
            status = 0
            connection.Connection.selectCustomers(status)

        if var.ui.rbtIndividual.isChecked():
            status = 1
            connection.Connection.selectCustomers(status)

        if var.ui.rbtBussiness.isChecked():
            status = 2
            connection.Connection.selectCustomers(status)
            
            
    
    @staticmethod
    def loadCustomersTable(register):
        try:
            index = 0
            for record in register:
                var.ui.tabCustomers.setRowCount(index + 1)
                var.ui.tabCustomers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(record[0])))
                var.ui.tabCustomers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(record[1])))
                var.ui.tabCustomers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(record[2])))
                var.ui.tabCustomers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(record[3])))
                var.ui.tabCustomers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(record[4])))
                var.ui.tabCustomers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(record[5])))
                var.ui.tabCustomers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error loading data into table', error)