from PyQt6 import QtWidgets, QtSql

import var
import datetime
import customers
import events


class Connection:
    @staticmethod
    def connection(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)

        if not db.open():
            print("Connection error")
            return False
        else:
            print("Connected database")
            return True



    @staticmethod
    def removeFireDate(codigo):
        try:
            query = QtSql.QSqlQuery()

            #COMPROBAR CONSULTA
            query.prepare("update customers set bajadri = null where codigo = :codigo")
            query.bindValue(':codigo', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer enrolled")
                mbox.exec()

        except Exception as error:
            print('error when removing fire date', error)



    @staticmethod
    def saveCustomer(newcustomer):
        try:
            print(newcustomer)
            query = QtSql.QSqlQuery()
            query.prepare('insert into customer (name_customer, surname_customer, address_customer, '
                              ' date_birthday_customer, telephone_customer, email_customer, category_customer) '
                              ' VALUES (:name, :surname, :address, :date_birthday, :telephone, :email, :category)')
            query.bindValue(':name', str(newcustomer[0]))
            query.bindValue(':surname', str(newcustomer[1]))
            query.bindValue(':address', str(newcustomer[2]))
            query.bindValue(':date_birthday', str(newcustomer[3]))
            query.bindValue(':telephone', str(newcustomer[4]))
            query.bindValue(':email', str(newcustomer[5]))
            query.bindValue(':category', str(newcustomer[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer enrolled")
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error saving customer")
                mbox.exec()

        except Exception as error:
            print("Error saving customer: ", error)



    def selectCustomers(status):
        try:
            record = []

            consulta = "select id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer from customer"

            if int(status) == 1:
                consulta = consulta + " where bajadri is null"

            elif int(status) == 2:
                consulta = consulta + " where bajadri is not null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    record.append(row)
            customers.Customers.loadCustomersTable(record)

        except Exception as error:
            print('error when selecting customer', error)
