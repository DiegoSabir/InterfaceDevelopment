from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var


class Products:
    @staticmethod
    def clear_products():
        try:
            widgetList = [var.ui.lblIdPro, var.ui.txtNamePro, var.ui.txtPricePro, var.ui.spStockPro]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear from products", error)



    @staticmethod
    def add_product():
        try:
            newproduct = [var.ui.txtNamePro.text(),
                          var.ui.txtPricePro.text(),
                          var.ui.spStockPro.text()]

            connection.Connection.save_product(newproduct)
            connection.Connection.show_products()

        except Exception as error:
            print("Error en addProduct from products", error)



    @staticmethod
    def load_products_table(register):
        try:
            index = 0
            for record in register:
                var.ui.tabProducts.setRowCount(index + 1)
                var.ui.tabProducts.setItem(index, 0, QtWidgets.QTableWidgetItem(str(record[0])))
                var.ui.tabProducts.setItem(index, 1, QtWidgets.QTableWidgetItem(str(record[1])))
                var.ui.tabProducts.setItem(index, 2, QtWidgets.QTableWidgetItem(str(record[2]) + ' € '))
                var.ui.tabProducts.setItem(index, 3, QtWidgets.QTableWidgetItem(str(record[3])))

                var.ui.tabProducts.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabProducts.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                var.ui.tabProducts.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabProducts.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error en loadProductsTable from products', error)



    @staticmethod
    def load_products():
        try:
            Products.clear_products()
            row = var.ui.tabProducts.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.one_product(fila[0])

            datos = [var.ui.lblIdPro,
                     var.ui.txtNamePro,
                     var.ui.txtPricePro,
                     var.ui.spStockPro]

            for i, dato in enumerate(datos):
                if isinstance(dato, QtWidgets.QSpinBox):
                    dato.setValue(int(registro[i]))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            print('error en loadProducts from products', error)



    def modify_product(self):
        try:
            modifyproduct = [var.ui.txtNamePro.text(),
                             var.ui.txtPricePro.text(),
                             var.ui.spStockPro.text()]

            connection.Connection.check_modify_product(modifyproduct)
            connection.Connection.show_products()

        except Exception as error:
            print('error en modifyProduct from products', error)



    def remove_product(self):
        try:
            codigo = var.ui.lblIdPro.text().title()

            connection.Connection.remove_product(codigo)
            Products.clear_products()
            connection.Connection.show_products()

        except Exception as error:
            print('error en removeProduct from products', error)
