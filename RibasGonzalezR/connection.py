from PyQt6 import QtWidgets, QtSql

import products
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
            Connection.selectCustomers()

        except Exception as error:
            print("error en showCustomer from connection", error)


    @staticmethod
    def oneCustomer(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from customer where id_customer = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
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


    @staticmethod
    def selectCustomers():
        try:
            if var.ui.chkAll.isChecked():
                consulta = 'select category_customer, name_customer, address_customer, telephone_customer, email_customerfrom customer WHERE firedate_customer is not null'

            else:
                consulta = 'select category_customer, name_customer, address_customer, telephone_customer, email_customer from customer WHERE firedate_customer is null'

            register = []

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    register.append(row)
            else:
                print(query.lastError())
            customers.Customers.loadCustomersTable(register)

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
    def addFireDate(codigo):
        try:
            date = datetime.date.today()
            date = date.strftime('%d/%m/%Y')
            query = QtSql.QSqlQuery()
            query.prepare("update customer set firedate_customer = :firedate where id_customer = :id")
            query.bindValue(':firedate', str(date))
            query.bindValue(':id', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer enrolled")
                mbox.exec()

        except Exception as error:
            print('error en addFireDate from connection', error)



    """
    METODOS DE PRODUCTOS
    """

    @staticmethod
    def saveProduct(newproduct):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into product (name_product, price_product, stock_product) VALUES (:name, :price, :stock)')
            query.bindValue(':name', str(newproduct[0]))
            query.bindValue(':price', str(newproduct[1]))
            query.bindValue(':stock', str(newproduct[2]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Product added")
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error saving product")
                mbox.exec()

        except Exception as error:
            print("Error en saveProduct from connection ", error)



    @staticmethod
    def showProducts():
        try:
            Connection.selectProducts()

        except Exception as error:
            print("error en showProducts from connection", error)



    def oneProduct(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from product where id_product = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en oneProduct from connection', error)



    @staticmethod
    def selectProducts():
        try:
            consulta = 'select id_product, name_product, price_product, stock_product from product'

            register = []

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    register.append(row)
            else:
                print(query.lastError())
            products.Products.loadProductsTable(register)

        except Exception as error:
            print('error en selectCustomers from connection', error)
