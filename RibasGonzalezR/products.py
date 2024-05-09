from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var


class Products:
    @staticmethod
    def clear():
        try:
            widgetList = [var.ui.lblIdPro, var.ui.txtNamePro, var.ui.txtPricePro, var.ui.spStockPro]
            for i in widgetList:
                i.clear()

            var.ui.chkAll.setChecked(False)

        except Exception as error:
            print("error en clear from products", error)



    @staticmethod
    def addProduct():
        try:
            newproduct = [var.ui.txtNamePro.text(),
                          var.ui.txtPricePro.text(),
                          var.ui.spStockPro.text()]

            connection.Connection.saveProduct(newproduct)
            connection.Connection.showProducts()

        except Exception as error:
            print("Error en addProduct from products", error)



    @staticmethod
    def loadProductsTable(register):
        try:
            index = 0
            for record in register:
                var.ui.tabProducts.setRowCount(index + 1)
                var.ui.tabProducts.setItem(index, 0, QtWidgets.QTableWidgetItem(str(record[0])))
                var.ui.tabProducts.setItem(index, 1, QtWidgets.QTableWidgetItem(str(record[1])))
                var.ui.tabProducts.setItem(index, 2, QtWidgets.QTableWidgetItem(str(record[2])))
                var.ui.tabProducts.setItem(index, 3, QtWidgets.QTableWidgetItem(str(record[3])))

                var.ui.tabProducts.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabProducts.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabProducts.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabProducts.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error en loadProductsTable from products', error)



    @staticmethod
    def loadProducts():
        try:
            Products.clear()
            selected_row = var.ui.tabProducts.currentRow()
            if selected_row != -1:
                id_product = var.ui.tabProducts.item(selected_row, 0).text()
                registro = connection.Connection.oneProduct(id_product)
                if registro:
                    datos = [var.ui.lblIdPro,
                             var.ui.txtNamePro,
                             var.ui.txtPricePro,
                             var.ui.spStockPro]

                    for dato, value in zip(datos, registro):
                        dato.setText(str(value))

        except Exception as error:
            print('error en loadProducts from products', error)
