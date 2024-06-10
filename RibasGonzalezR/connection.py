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
        """
        Establece la conexión con la base de datos SQLite.

        :param self: Parámetro opcional.
        :return: True si la conexión es exitosa, False en caso contrario.
        """
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
    def save_customer(newcustomer):
        """
        Guarda un nuevo cliente en la base de datos.

        :param newcustomer: Lista con los datos del nuevo cliente.
        :return: None
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO customer (name_customer, surname_customer, address_customer, '
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
            print("Error en save_customer from connection ", error)



    @staticmethod
    def show_customers():
        """
        Muestra todos los clientes en la interfaz de usuario.

        :return: None
        """
        try:
            Connection.select_customers()

        except Exception as error:
            print("error en show_customers from connection", error)



    @staticmethod
    def one_customer(id):
        """
        Obtiene los datos de un cliente específico por su ID.

        :param id: ID del cliente.
        :return: Lista con los datos del cliente.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM customer WHERE id_customer = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(9):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en one_customer from connection', error)



    @staticmethod
    def check_modify_customer(modifycustomer):
        """
        Verifica y modifica los datos de un cliente.

        :param modifycustomer: Lista con los datos del cliente modificados.
        :return: None
        """
        try:
            codigo = var.ui.lblId.text()

            Connection.modify_customer(modifycustomer, codigo)

        except Exception as error:
            print("error en check_modify_customer from connection", error)



    @staticmethod
    def modify_customer(modifycustomer, codigo):
        """
        Modifica los datos de un cliente en la base de datos.

        :param modifycustomer: Lista con los datos del cliente modificados.
        :param codigo: ID del cliente.
        :return: None
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE customer SET id_customer = :id, name_customer = :name ,surname_customer = :surname, address_customer = :address, '
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
            print('error en modify_customer from connection', error)



    @staticmethod
    def select_customers():
        """
        Selecciona y carga los datos de los clientes en la tabla de la interfaz de usuario.

        :return: None
        """
        try:
            consulta = ''
            if var.ui.rbtIndividual.isChecked():
                if var.ui.chkAll.isChecked():
                    consulta = 'SELECT id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer, firedate_customer FROM customer WHERE category_customer IS "Individual"'

                else:
                    consulta = 'SELECT id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer, firedate_customer FROM customer WHERE firedate_customer IS NULL AND category_customer IS "Individual"'

            elif var.ui.rbtBusiness.isChecked():
                if var.ui.chkAll.isChecked():
                    consulta = 'SELECT id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer, firedate_customer FROM customer WHERE category_customer IS "Bussiness"'

                else:
                    consulta = 'SELECT id_customer, category_customer, name_customer, address_customer, telephone_customer, email_customer, firedate_customer FROM customer WHERE firedate_customer IS NULL AND category_customer IS "Bussiness"'

            register = []

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    register.append(row)
            else:
                print(query.lastError())

            customers.Customers.load_customers_table(register)

        except Exception as error:
            print('error en select_customers from connection', error)



    @staticmethod
    def select_all_customers():
        """
        Selecciona todos los clientes de la base de datos ordenados por apellido.

        :return: Lista de registros de clientes.
        """
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM customer ORDER BY surname_customer')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('error en select_all_customers from connection', error)



    @staticmethod
    def add_fire_date(codigo):
        """
        Añade la fecha de baja a un cliente en la base de datos.

        :param codigo: ID del cliente.
        :return: None
        """
        try:
            date = datetime.date.today()
            date = date.strftime('%d/%m/%Y')
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE customer SET firedate_customer = :firedate WHERE id_customer = :id")
            query.bindValue(':firedate', str(date))
            query.bindValue(':id', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Customer fired")
                mbox.exec()

        except Exception as error:
            print('error en add_fire_date from connection', error)



    @staticmethod
    def check_fire_customer(codigo):
        """
        Verifica si un cliente está dado de baja.

        :param codigo: ID del cliente.
        :return: True si el cliente está dado de baja, False en caso contrario.
        """
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
            print("error en check_fire_customer from connection", error)
            return False



    """
    --------------------------------------------------------------------------------------------------------------------
    
    PRODUCTS METHODS
    
    --------------------------------------------------------------------------------------------------------------------
    """

    @staticmethod
    def save_product(newproduct):
        """
        Guarda un nuevo producto en la base de datos.

        :param newproduct: Lista con los datos del nuevo producto.
        :return: None
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO product (name_product, price_product, stock_product) VALUES (:name, :price, :stock)')
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
            print("Error en save_product from connection ", error)



    @staticmethod
    def show_products():
        """
        Muestra todos los productos en la interfaz de usuario.

        :return: None
        """
        try:
            Connection.select_products()

        except Exception as error:
            print("error en show_products from connection", error)



    def one_product(id):
        """
        Obtiene los datos de un producto específico por su ID.

        :param id: ID del producto.
        :return: Lista con los datos del producto.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM product WHERE id_product = :id')
            query.bindValue(':id', int(id))

            if query.exec():
                while query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en one_product from connection', error)



    @staticmethod
    def select_products():
        """
        Selecciona y carga los datos de los productos en la tabla de la interfaz de usuario.

        :return: None
        """
        try:
            consulta = 'SELECT id_product, name_product, price_product, stock_product FROM product'

            register = []

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    register.append(row)
            else:
                print(query.lastError())
            products.Products.load_products_table(register)

        except Exception as error:
            print('error en select_products from connection', error)



    @staticmethod
    def check_modify_product(modifyproduct):
        """
        Verifica y modifica los datos de un producto.

        :param modifyproduct: Lista con los datos del producto modificados.
        :return: None
        """
        try:
            codigo = var.ui.lblIdPro.text()

            Connection.modify_product(modifyproduct, codigo)

        except Exception as error:
            print("error en check_modify_product from connection", error)



    @staticmethod
    def modify_product(modifyproduct, codigo):
        """
        Modifica los datos de un producto en la base de datos.

        :param modifyproduct: Lista con los datos del producto modificados.
        :param codigo: ID del producto.
        :return: None
        """
        try:
            # Obtener el stock actual del producto seleccionado
            current_stock = var.ui.spStockPro.value()

            query = QtSql.QSqlQuery()
            query.prepare('UPDATE product SET id_product = :id, name_product = :name, price_product = :price, '
                          'stock_product = :stock WHERE id_product = :id')

            query.bindValue(':id', int(codigo))
            query.bindValue(':name', str(modifyproduct[0]))
            query.bindValue(':price', str(modifyproduct[1]))

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
            print('error en modify_product from connection', error)



    def remove_product(idProduct):
        """
        Elimina un producto de la base de datos por su ID.

        :param idProduct: ID del producto.
        :return: True si la eliminación es exitosa, False en caso contrario.
        """
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
            print('error en remove_product from connection', error)



    """
    --------------------------------------------------------------------------------------------------------------------

    INVOICE METHODS

    --------------------------------------------------------------------------------------------------------------------
    """
    def load_customer(self=None):
        """
        Carga los clientes en el comboBox de la interfaz de usuario para selección.

        :param self: Parámetro opcional.
        :return: None
        """
        try:
            var.ui.cmbIdCustomer.clear()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_customer, name_customer FROM customer ORDER BY id_customer')
            if query.exec():
                var.ui.cmbIdCustomer.addItem('')

                while query.next():
                    var.ui.cmbIdCustomer.addItem(f"{query.value(0)}. {query.value(1)}")
            else:
                raise Exception("Query execution failed")

        except Exception as error:
            print(f"error en load_customer from connection: {error}")



    def save_invoice(registro):
        """
        Guarda una nueva factura en la base de datos.

        :param registro: Lista con los datos de la factura.
        :return: None
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO invoice (customer_invoice, date_invoice) VALUES (:customer, :date)')
            query.bindValue(":customer", str(registro[0]))
            query.bindValue(":date", str(registro[1]))
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Saved invoice")
                mbox.exec()

            else:
                raise Exception(query.lastError().text())

            Connection.load_invoice()

        except Exception as error:
            print("error en save_invoice from connection", error)



    @staticmethod
    def load_invoice():
        """
        Carga las facturas en la tabla de la interfaz de usuario.

        :return: None
        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id_invoice, customer_invoice, date_invoice FROM invoice")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)

            invoices.Invoices.load_invoice_tab(registros)

        except Exception as error:
            print("error en load_invoice from connection", error)



    @staticmethod
    def one_invoice(id):
        """
        Obtiene los datos de una factura específica por su ID.

        :param id: ID de la factura.
        :return: Lista con los datos de la factura.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM invoice WHERE id_invoice = :id')
            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(3):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("error en one_invoice from connection", error)



    def load_product(self=None):
        """
        Carga los productos en el comboBox de la interfaz de usuario para selección.

        :param self: Parámetro opcional.
        :return: None
        """
        try:
            var.ui.cmbIdProductSale.clear()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_product, name_product FROM product ORDER BY id_product')
            if query.exec():
                var.ui.cmbIdProductSale.addItem('')
                while query.next():
                    var.ui.cmbIdProductSale.addItem(f"{query.value(0)}. {query.value(1)}")
            else:
                raise Exception("Query execution failed")

        except Exception as error:
            print(f"error en load_product from connection: {error}")



    def save_sale(registro):
        """
        Guarda una nueva venta en la base de datos.

        :param registro: Lista con los datos de la venta.
        :return: None
        """
        try:
            idProducto = registro[1]
            precio = Connection.get_price(idProducto)
            newReg = []
            for i in registro:
                newReg.append(i)
            newReg.append(precio)
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO sale (id_invoice_sale, id_product_sale, quantity_sale, price_sale) VALUES (:id_invoice, :id_product, :quantity, :price)')
            query.bindValue(":id_invoice", int(newReg[0]))
            query.bindValue(":id_product", int(newReg[1]))
            query.bindValue(":quantity", int(newReg[2]))
            query.bindValue(":price", str(newReg[3]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Information')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Added sale")
                mbox.exec()

            else:
                raise Exception(query.lastError().text())

            Connection.load_sale(query)

        except Exception as error:
            print("error en save_sale from connection:", error)



    def get_price(idProducto):
        """
        Obtiene el precio de un producto específico por su ID.

        :param idProducto: ID del producto.
        :return: Precio del producto.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT price_product FROM product WHERE id_product = :id')
            query.bindValue(":id", str(idProducto))
            if query.exec():
                while query.next():
                    precio = query.value(0)
                    return precio
            print(query.lastError().text())

        except Exception as error:
            print("error en get_price from connection:", error)



    @staticmethod
    def load_sale(dato):
        """
        Carga las ventas relacionadas con una factura específica en la tabla de la interfaz de usuario.

        :param dato: ID de la factura.
        :return: None
        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT sale.id_sale, sale.id_invoice_sale, product.name_product, sale.quantity_sale, sale.price_sale, (sale.quantity_sale * sale.price_sale) AS total FROM sale INNER JOIN product ON sale.id_product_sale = product.id_product WHERE id_invoice_sale = :dato")
            query.bindValue(':dato', dato)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)

            invoices.Invoices.load_sale_tab(registros)

        except Exception as error:
            print("error en load_sale from connection:", error)



    @staticmethod
    def one_sale(id):
        """
        Obtiene los datos de una venta específica por su ID.

        :param id: ID de la venta.
        :return: Lista con los datos de la venta.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id_sale, id_invoice_sale, id_product_sale, quantity_sale FROM sale WHERE id_sale = :id')
            query.bindValue(':id', int(id))

            if query.exec():
                if query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("error en one_sale from connection:", error)



    def modify_sale(sale):
        """
        Modifica los datos de una venta en la base de datos.

        :param sale: Lista con los datos de la venta modificada.
        :return: True si la modificación es exitosa, False en caso contrario.
        """
        try:
            consulta = ('UPDATE sale SET id_product_sale = :id_product, quantity_sale = :quantity WHERE id_sale = :id')

            query = QtSql.QSqlQuery()
            query.prepare(consulta)
            query.bindValue(':id', int(sale[0]))
            query.bindValue(':id_product', str(sale[1]))
            query.bindValue(':quantity', int(sale[2]))

            if query.exec():
                return True

            else:
                print(query.lastError().text())
                return False

        except Exception as error:
            print("error en modify_sale from connection:", error)
