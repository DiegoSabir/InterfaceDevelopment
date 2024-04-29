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
    def saveCustomer(newcustomer):
        try:
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
            print("Error en saveCustomer from connection ", error)


    @staticmethod
    def showCustomers():
        try:
            estado = 1
            Connection.selectCustomers(estado)

        except Exception as error:
            print("error ao cargar a tabla", error)



    def oneCustomer(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from customer where id_customer = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en oneCustomer from connection', error)



    def checkModifyCustomer(modifycustomer):
        try:
            codigo = var.ui.lblId.text()

            if customers.Customers.checkFireDate(codigo):
                events.Events.showFireModify()
                Connection.modifyCustomer(modifycustomer)

            else:
                Connection.modifyCustomer(modifycustomer)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer data changed")
                mbox.exec()

        except Exception as error:
            print("error en checkModifyCustomer from conexion", error)



    @staticmethod
    def modifyCustomer(modifycustomer):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update customer set id_customer = :id, name_customer = :name ,surname_customer = :surname, address_customer = :address, '
                          'date_birthday_customer = :date_birthday, telephone_customer = :telephone, email_customer = :email,'
                          'category_customer = :category where id_customer = :id')

            query.bindValue(':id', str(modifycustomer[0]))
            query.bindValue(':name', str(modifycustomer[1]))
            query.bindValue(':surname', str(modifycustomer[2]))
            query.bindValue(':address', str(modifycustomer[3]))
            query.bindValue(':date_birthday', str(modifycustomer[4]))
            query.bindValue(':telephone', str(modifycustomer[5]))
            query.bindValue(':email', str(modifycustomer[6]))
            query.bindValue(':category', str(modifycustomer[7]))

            if query.exec():
                customers.Customers.selectStatus()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al modificar los datos del conductor")
                mbox.exec()

        except Exception as error:
            print('error en modifyCustomer from connection', error)



    def selectCustomers(status):
        try:
            record = []

            consulta = "select category_customer, name_customer, address_customer, telephone_customer, email_customer from customer"

            if int(status) == 1:
                consulta = consulta + " where firedate_customer is null"

            elif int(status) == 2:
                consulta = consulta + " where firedate_customer is not null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    record.append(row)
            customers.Customers.loadCustomersTable(record)

        except Exception as error:
            print('error en selectCustomers from connection', error)


    @staticmethod
    def selectAllCustomers():
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('Select * from customer order by surname_customer')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('error en selectAllCustomers from connection', error)



    @staticmethod
    def removeFireDate(codigo):
        try:
            query = QtSql.QSqlQuery()

            query.prepare("update customer set firedate_customer = null where id_customer = :id")
            query.bindValue(':id', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer enrolled")
                mbox.exec()

        except Exception as error:
            print('error en removeFireDate from connection', error)
