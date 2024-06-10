from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var
import re


class Customers:
    @staticmethod
    def load_date(qDate):
        """
        Carga una fecha dada en la interfaz de usuario y oculta el widget del calendario.

        :param qDate: Objeto QDate que representa la fecha a cargar.
        :return: None
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtEnrollDate.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en load_date from customers", error)



    @staticmethod
    def load_fire_date(qDate):
        """
        Carga una fecha de baja en la interfaz de usuario, actualiza la base de datos con la fecha de baja,
        y oculta el calendario y la ventana de modificación.

        :param qDate: Objeto QDate que representa la fecha de baja a cargar.
        :return: None
        """
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
        """
        Limpia todos los campos de información del cliente en la interfaz de usuario.

        :return: None
        """
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
        """
        Registra un nuevo cliente o actualiza la fecha de baja de un cliente existente en la base de datos.

        :return: None
        """
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
        """
        Carga los datos de los clientes en la tabla de la interfaz de usuario.

        :param register: Lista de registros de clientes a cargar.
        :return: None
        """
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
        """
        Carga los datos del cliente seleccionado en los campos de información de la interfaz de usuario.

        :return: None
        """
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
        """
        Modifica los datos del cliente en la base de datos con la información actual de la interfaz de usuario.

        :return: None
        """
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
            print("error en modify_customer from customers", error)



    @staticmethod
    def check_fire_date(codigo):
        """
        Verifica si un cliente tiene una fecha de baja registrada en la base de datos.

        :param codigo: Código del cliente a verificar.
        :return: True si el cliente tiene una fecha de baja, False en caso contrario.
        """
        try:
            baja = True
            query = QtSql.QSqlQuery()
            query.prepare("SELECT firedate_customer FROM customer WHERE id_customer = :id")
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
        """
        Modifica la fecha de baja de un cliente en la base de datos.

        :param codigo: Código del cliente a modificar.
        :param fecha: Nueva fecha de baja.
        :return: None
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE customer SET firedate_customer = :firedate WHERE id_customer = :id")

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
        """
        Marca a un cliente como dado de baja en la base de datos.

        :return: None
        """
        try:
            codigo = var.ui.lblId.text()
            if connection.Connection.check_fire_customer(codigo):
                print("El cliente ya está dado de baja.")
                return

            else:
                connection.Connection.add_fire_date(codigo)
            connection.Connection.show_customers()

        except Exception as error:
            print("Error en fire_customer from customer ", error)
