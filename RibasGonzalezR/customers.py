from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var
import re


class Customers:
    @staticmethod
    def load_date(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtEnrollDate.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en load_date from customers", error)



    @staticmethod
    def load_fire_date(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            codigo = var.ui.lblId.text()
            Customers.modify_fire_date(codigo, data)
            var.calendar.hide()
            var.dlgModifyFireWindow.hide()

        except Exception as error:
            print("error en load_fire_date from customers", error)



    @staticmethod
    def clear():
        try:
            widgetList = [var.ui.lblId, var.ui.txtSurname, var.ui.txtName, var.ui.txtAddress, var.ui.txtEmail,
                          var.ui.txtEnrollDate, var.ui.txtTelephone]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear from customers", error)



    @staticmethod
    def enroll_customer():
        try:
            if var.ui.lblId.text() != "":
                codigo = var.ui.lblId.text()
                if Customers.check_fire_date(codigo):
                    connection.Connection.add_fire_date(codigo)
            else:
                newcustomer = [var.ui.txtName.text(),
                               var.ui.txtSurname.text(),
                               var.ui.txtAddress.text(),
                               var.ui.txtEnrollDate.text(),
                               var.ui.txtTelephone.text(),
                               var.ui.txtEmail.text()]

                if var.ui.rbtIndividual.isChecked():
                    newcustomer.append("Individual")
                elif var.ui.rbtBusiness.isChecked():
                    newcustomer.append("Bussiness")

                connection.Connection.save_customer(newcustomer)
                connection.Connection.show_customers()

        except Exception as error:
            print("Error en enroll_customer from customers", error)



    @staticmethod
    def load_customers_table(register):
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
                var.ui.tabCustomers.setItem(index, 6, QtWidgets.QTableWidgetItem(str(record[6])))

                var.ui.tabCustomers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabCustomers.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error en load_customers_table from customers', error)



    @staticmethod
    def load_customers():
        try:
            Customers.clear()
            row = var.ui.tabCustomers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.one_customer(fila[0])

            datos = [var.ui.lblId,
                     var.ui.txtName,
                     var.ui.txtSurname,
                     var.ui.txtAddress,
                     var.ui.txtEnrollDate,
                     var.ui.txtTelephone,
                     var.ui.txtEmail]

            for i, dato in enumerate(datos):
                dato.setText(str(registro[i]))

            if 'Individual' in registro[7]:
                var.ui.rbtIndividual.setChecked(True)
            if 'Bussiness' in registro[7]:
                var.ui.rbtBusiness.setChecked(True)

        except Exception as error:
            print('error en load_customers from customers', error)



    @staticmethod
    def modify_customer():
        try:
            modifycustomer = [var.ui.txtName.text(),
                              var.ui.txtSurname.text(),
                              var.ui.txtAddress.text(),
                              var.ui.txtEnrollDate.text(),
                              var.ui.txtTelephone.text(),
                              var.ui.txtEmail.text()]

            if var.ui.rbtIndividual.isChecked():
                modifycustomer.append("Individual")
            elif var.ui.rbtBusiness.isChecked():
                modifycustomer.append("Bussiness")

            connection.Connection.check_modify_customer(modifycustomer)

        except Exception as error:
            print("error en modifyCustomer from customers", error)



    @staticmethod
    def check_fire_date(codigo):
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
            print('error en check_fire_date from customers', error)



    @staticmethod
    def modify_fire_date(codigo, fecha):
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

        except Exception as error:
            print('error en modify_fire_date from customers', error)



    def fire_customer(self):
        try:
            codigo = var.ui.lblId.text()
            if connection.Connection.fire_customer(codigo):
                print("El cliente ya está dado de baja.")
                return

            else:
                connection.Connection.add_fire_date(codigo)
            connection.Connection.show_customers()

        except Exception as error:
            print("Error en fire_customer from customer ", error)
