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
            print("error en validateEmail from customers", error)



    @staticmethod
    def loadDate(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtBirthdate.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en loadDate from customers", error)



    @staticmethod
    def loadFireDate(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            codigo = var.ui.lblId.text()
            Customers.modifyFireDate(codigo, data)
            var.calendar.hide()
            var.dlgModifyFireWindow.hide()

        except Exception as error:
            print("error en loadFireDate from customers", error)



    @staticmethod
    def clear():
        try:
            widgetList = [var.ui.lblId, var.ui.txtSurname, var.ui.txtName, var.ui.txtAddress, var.ui.txtEmail,
                            var.ui.txtBirthdate, var.ui.txtTelephone]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear from customers", error)



    @staticmethod
    def enrollCustomer():
        try:
            if var.ui.lblId.text() != "":
                codigo = var.ui.lblId.text()
                if Customers.checkFireDate(codigo):
                    connection.Connection.removeFireDate(codigo)
                    Customers.selectStatus()
            else:
                newcustomer = [var.ui.txtName.text(),
                               var.ui.txtSurname.text(),
                               var.ui.txtAddress.text(),
                               var.ui.txtBirthdate.text(),
                               var.ui.txtTelephone.text(),
                               var.ui.txtEmail.text()]

                if var.ui.rbtIndividual.isChecked():
                    newcustomer.append("Individual")
                elif var.ui.rbtBussiness.isChecked():
                    newcustomer.append("Bussiness")

                connection.Connection.saveCustomer(newcustomer)

        except Exception as error:
            print("Error en enrollCustomer from customers", error)



    @staticmethod
    def selectStatus():
        if var.ui.chkAll.isChecked():
            status = 0

        elif var.ui.rbtIndividual.isChecked():
            status = 1

        elif var.ui.rbtBussiness.isChecked():
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
            print('error en loadCustomersTable from customers', error)



    @staticmethod
    def loadCustomers():
        try:
            Customers.clear()

            row = var.ui.tabCustomers.selectedItems()

            fila = [dato.text() for dato in row]
            registro = connection.Connection.oneCustomer(fila[0])

            datos = [var.ui.txtName,
                     var.ui.txtSurname,
                     var.ui.txtAddress,
                     var.ui.txtBirthdate,
                     var.ui.txtTelephone,
                     var.ui.txtEmail]

            for i, dato in enumerate(datos):
                dato.setText(str(registro[i]))

        except Exception as error:
            print('error en loadCustomers from customers', error)



    @staticmethod
    def modifyCustomer():
        try:
            customer = [var.ui.txtName,
                        var.ui.txtSurname,
                        var.ui.txtAddress,
                        var.ui.txtBirthdate,
                        var.ui.txtTelephone,
                        var.ui.txtEmail]

            modifcustomer = []
            for i in customer:
                modifcustomer.append(i.text().title())

            connection.Connection.checkModifyCustomer(modifcustomer)

        except Exception as error:
            print("error en modifyCustomer from customers", error)



    @staticmethod
    def checkFireDate(codigo):
        try:
            baja = True
            query = QtSql.QSqlQuery()
            query.prepare("select firedate_customer from customer where id_customer = :id")
            query.bindValue(':id', int(codigo))
            if query.exec():
                while query.next():
                    fecha = query.value(0)
                    if fecha == "":
                        baja = False
            return baja

        except Exception as error:
            print('error en checkFireDate from customers', error)



    @staticmethod
    def modifyFireDate(codigo, fecha):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update customer set firedate_customer = :firedate where id_customer = :id")

            query.bindValue(':id', int(codigo))
            query.bindValue(':firedate', str(fecha))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Modified Data")
                mbox.exec()

                Customers.selectStatus()

        except Exception as error:
            print('error en modifyFireDate from customers', error)
