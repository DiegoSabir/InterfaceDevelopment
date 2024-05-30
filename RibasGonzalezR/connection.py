from PyQt6 import QtWidgets, QtSql

import invoices
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
                              ' enrolldate_customer, telephone_customer, email_customer, category_customer) '
                              ' VALUES (:name, :surname, :address, :enrolldate, :telephone, :email, :category)')
            query.bindValue(':name', str(newcustomer[0]))
            query.bindValue(':surname', str(newcustomer[1]))
            query.bindValue(':address', str(newcustomer[2]))
            query.bindValue(':enrolldate', str(newcustomer[3]))
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
                    for i in range(9):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en oneCustomer from connection', error)


    @staticmethod
    def checkModifyCustomer(modifycustomer):
        try:
            codigo = var.ui.lblId.text()

            Connection.modifyCustomer(modifycustomer, codigo)

        except Exception as error:
            print("error en checkModifyCustomer from connection", error)



    @staticmethod
    def modifyCustomer(modifycustomer, codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update customer set id_customer = :id, name_customer = :name ,surname_customer = :surname, address_customer = :address, '
                          'enrolldate_customer = :enrolldate, telephone_customer = :telephone, email_customer = :email,'
                          'category_customer = :category where id_customer = :id')

            query.bindValue(':id', int(codigo))
            query.bindValue(':name', str(modifycustomer[0]))
            query.bindValue(':surname', str(modifycustomer[1]))
            query.bindValue(':address', str(modifycustomer[2]))
            query.bindValue(':enrolldate', str(modifycustomer[3]))
            query.bindValue(':telephone', str(modifycustomer[4]))
            query.bindValue(':email', str(modifycustomer[5]))
            query.bindValue(':category', str(modifycustomer[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Modified customer data")
                mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error when modifying driver data")
                mbox.exec()

        except Exception as error:
            print('error en modifyCustomer from connection', error)



    @staticmethod
    def selectCustomers():
        try:
            if var.ui.chkAll.isChecked():
                consulta = 'select id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer from customer'

            else:
                consulta = 'select id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer from customer WHERE firedate_customer is null'

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
                mbox.setText("Customer fired")
                mbox.exec()

        except Exception as error:
            print('error en addFireDate from connection', error)



    @staticmethod
    def clienteEstaDadoDeBaja(codigo):
        try:
            consulta = "SELECT COUNT(*) FROM customer WHERE id_customer = ? AND firedate_customer IS NOT NULL"
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.addBindValue(codigo)
            if query.exec() and query.next():
                return query.value(0) > 0  # If count > 0, client is marked as inactive
            else:
                return False  # Assuming no result means the client is not marked as inactive

        except Exception as error:
            print("error en clienteEstaDadoDeBaja from connection", error)
            return False



    """
    --------------------------------------------------------------------------------------------------------------------
    
    PRODUCTS METHODS
    
    --------------------------------------------------------------------------------------------------------------------
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
                    for i in range(4):
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
            print('error en selectProducts from connection', error)



    @staticmethod
    def checkModifyProduct(modifyproduct):
        try:
            codigo = var.ui.lblIdPro.text()

            Connection.modifyProduct(modifyproduct, codigo)

        except Exception as error:
            print("error en checkModifyProduct from connection", error)



    @staticmethod
    def modifyProduct(modifyproduct, codigo):
        try:
            # Obtener el stock actual del producto seleccionado
            current_stock = var.ui.spStockPro.value()

            query = QtSql.QSqlQuery()
            query.prepare('update product set id_product = :id, name_product = :name, price_product = :price, '
                          'stock_product = :stock where id_product = :id')

            query.bindValue(':id', int(codigo))
            query.bindValue(':name', str(modifyproduct[0]))
            query.bindValue(':price', str(modifyproduct[1]))
            #query.bindValue(':stock', int(modifyproduct[2]))

            # Calcular el nuevo stock utilizando la diferencia entre el stock actual y el stock modificado
            new_stock = int(modifyproduct[2]) + (current_stock - int(modifyproduct[2]))
            query.bindValue(':stock', new_stock)

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Modified product data")
                mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Warning')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error modifying product data")
                mbox.exec()

        except Exception as error:
            print('error en modifyProduct from connection', error)



    def removeProduct(idProduct):
        try:
            consulta = 'DELETE FROM product WHERE id_product = :id'
            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':id', int(idProduct))

            if query.exec():
                return True
            else:
                print(query.lastError().text())
                return False

        except Exception as error:
            print('error en removeProduct from connection', error)



    """
    --------------------------------------------------------------------------------------------------------------------

    INVOICE METHODS

    --------------------------------------------------------------------------------------------------------------------
    """
    def enroll_invoice(registro):
        try:
            print(registro)
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO invoices (id_customer_invoice, date_invoice) VALUES (:id_customer, :date)")
            query.bindValue(":id_customer", str(registro[0]))
            query.bindValue(":date", str(registro[1]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Information")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Factura creada correctamente.")
                mbox.exec()
                #Conexion.selectFactura()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Warning")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("La factura no se pudo crear.")
                mbox.exec()

        except Exception as error:
            print("error en enroll_invoice from connection", error)



    @staticmethod
    def getSurnameByCode(code : str):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select apeldri from drivers where codigo = :codigo")
            query.bindValue(":codigo", int(code))

            if query.exec():
                while query.next():
                    return query.value(0)
            else:
                print(query.lastError())

        except Exception as error:
            print("error en getSurnameByCode ", error)



    def oneInvoice(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from facturas where numfac = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
                return registro

            else:
                print("error en query onefac ", query.lastError())

        except Exception as error:
            print('error en fichero conexion dato de 1 factura ', error)



    @staticmethod
    def show_invoices():
        try:
            Connection.select_invoice()

        except Exception as error:
            print("error en show_invoices from connection", error)



    @staticmethod
    def select_invoice():
        try:

            registro = []

            consulta = "select id_invoice, id_customer_invoice, date_invoice from invoice"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)
            else:
                print(query.lastError())

            invoices.Invoices.load_invoice_table(registro)

        except Exception as error:
            print("error en select_invoice from connection", error)



    def select_customer_id(self=None):
        try:
            var.ui.cmbIdCustomer.clear()
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id_customer, name_customer FROM customer WHERE fire_date_customer IS NULL ORDER BY id_customer")
            if query.exec():
                var.ui.cmbIdCustomer.addItem('')
                while query.next():
                    var.ui.cmbIdCustomer.addItem(f'{query.value(0)}. {query.value(1)}')
            else:
                raise Exception("Query execution failed")

        except Exception as error:
            print("error en select_customer_id from connection", error)
